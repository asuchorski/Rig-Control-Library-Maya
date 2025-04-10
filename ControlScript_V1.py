import maya.cmds as cmds
import os

def import_control(control_name, base_dir, color_slider, color_display):
    # Import the specified control file from the base directory into the current scene
    file_path = os.path.join(base_dir, f"{control_name}.ma")
    
    if not os.path.exists(file_path):
        cmds.warning(f"File does not exist: {file_path}")
        return

    # Import the specified control file
    try:
        cmds.file(file_path, i=True, type="mayaAscii", ignoreVersion=True, ra=True, 
                  mergeNamespacesOnClash=False, options="v=0", pr=True)
        apply_color(color_slider, color_display)
    except Exception as e:
        cmds.warning(f"Failed to import {control_name}: {e}")
                
def set_selected_controls_color_and_line_width(color_index, line_width):
    """Set the color and line width of selected controls."""
    selected_controls = cmds.ls(selection=True)
    
    if not selected_controls:
        cmds.warning("No controls selected. Please select NURBS curves.")
        return
    
    for control in selected_controls:
        if cmds.objectType(control) == "transform":
            shape_nodes = cmds.listRelatives(control, shapes=True, fullPath=True) or []
            for shape_node in shape_nodes:
                enable_color_override(shape_node)
                set_control_color(shape_node, color_index)
                set_control_line_width(shape_node, line_width)
        else:
            enable_color_override(control)
            set_control_color(control, color_index)
            set_control_line_width(control, line_width)

def enable_color_override(control):
    """Enable the color override for a specific control."""
    try:
        cmds.setAttr(f"{control}.overrideEnabled", 1)
    except RuntimeError as e:
        cmds.warning(f"Failed to enable color override for {control}: {e}")

def set_control_color(control, color_index):
    """Set the color override for a specific control."""
    try:
        cmds.setAttr(f"{control}.overrideColor", color_index)
    except RuntimeError as e:
        cmds.warning(f"Failed to set color for {control}: {e}")

def set_control_line_width(control, line_width):
    """Set the line width for a specific control."""
    try:
        cmds.setAttr(f"{control}.lineWidth", line_width)
    except RuntimeError as e:
        cmds.warning(f"Failed to set line width for {control}: {e}")

def apply_color_and_line_width(color_slider, color_display, width_slider):
    """Apply the selected color and line width to the controls."""
    color_index = cmds.intSliderGrp(color_slider, query=True, value=True)
    line_width = cmds.floatSliderGrp(width_slider, query=True, value=True)
    set_selected_controls_color_and_line_width(color_index, line_width)
    cmds.colorSliderGrp(color_display, edit=True, rgb=cmds.colorIndex(color_index, q=True))

def update_color_display(color_slider, color_display, event):
    """Update the color display as the user slides the color_slider."""
    color_index = cmds.intSliderGrp(color_slider, query=True, value=True)
    cmds.colorSliderGrp(color_display, edit=True, rgb=cmds.colorIndex(color_index, q=True))
    
def createLocator():
    # Create locator at position of selected object
    selected_objects = cmds.ls(selection=True)
        
    # Create a locator
    locator = cmds.spaceLocator(name="Locator")
    
    # Get the translation of the selected object in world space
    position = cmds.xform(selected_objects, query=True, worldSpace=True, translation=True)
    
    # Get the rotation of the selected object in world space
    rotation = cmds.xform(selected_objects, query=True, worldSpace=True, rotation=True)
        
    # Move the locator to the position of the selected object
    cmds.xform(locator, worldSpace=True, translation=position)
    cmds.xform(locator, worldSpace=True, rotation=rotation)

def create_import_ui():
    # Create a UI for importing NURBS curve controls
    window_name = "importControlsUI"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name, window=True)

    window = cmds.window(window_name, title="Import Rig Controls", sizeable=True, 
                         widthHeight=(1, 10), backgroundColor=(0.2, 0.2, 0.25))
    
    # List of available controls
    controls = ["circleCtrl", "cubeCtrl", "arrowCtrl", "worldCtrl", "circleRotateCtrl", 
                "cylinderCtrl", "circlePinchedCtrl", "squareCtrl", "scapulaCtrl", 
                "translateCtrl", "sphereCtrl"]
    numControls = len(controls)
    
    cmds.rowColumnLayout(adjustableColumn=True, rowSpacing=(5, 5), 
                         numberOfColumns=2, columnWidth=[(1, 10), (2, 50)])

    base_dir = "C:\\Users\\Asuch\\Desktop\\Scripts\\Scenes"
    base_dir_img = "C:\\Users\\Asuch\\Desktop\\Scripts\\Imgs\\"

    for control in controls:
        cmds.button(label=f"{control}", 
                    command=lambda x, ctrl=control: import_control(ctrl, base_dir, color_slider, color_display), 
                    height=10)
        cmds.iconTextButton(style='iconOnly', w=50, h=50, image=base_dir_img + control + ".png")
        print(base_dir_img + control)
        
    
    
    # Add a banner titled "Color Override" before the color settings
    cmds.setParent('..')  # Close the rowColumnLayout
    
    
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="Create Locator", command=lambda x: createLocator(), backgroundColor=(0.1,0.1,0.2))
    cmds.separator(height=10, style='none')
    cmds.text(label="Color Override", align="center", font="boldLabelFont", height=20)
    cmds.separator(height=10, style='none')

    # Valid color indices for color override
    valid_color_indices = list(range(32))

    # Create stepped slider for color picking
    color_slider = cmds.intSliderGrp(label="Pick a Color", field=True, minValue=1, maxValue=31, value=0, step=1, fieldMinValue=1, fieldMaxValue=31,
                                     dragCommand=lambda x: update_color_display(color_slider, color_display, x))

    # Create color display
    color_display = cmds.colorSliderGrp(label="Selected Color", rgb=(0, 0, 0))
    # Create slider for line width
    width_slider = cmds.floatSliderGrp(label="Set Line Width", field=True, minValue=1.0, maxValue=10.0, value=1.0, step=0.1)
    
    cmds.separator(height=10, style='none')

   # Create apply button
    apply_button = cmds.button(label="Apply", command=lambda x: apply_color_and_line_width(color_slider, color_display, width_slider))

    cmds.showWindow(window)

# Run the UI creation function
create_import_ui()
