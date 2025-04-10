//Maya ASCII 2022 scene
//Name: cube.ma
//Last modified: Fri, Jun 21, 2024 03:50:17 PM
//Codeset: 1252
requires maya "2022";
requires "stereoCamera" "10.0";
requires "mtoa" "5.0.0.4";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2022";
fileInfo "version" "2022";
fileInfo "cutIdentifier" "202405021833-753375ecb3";
fileInfo "osv" "Windows 10 Pro v2009 (Build: 22631)";
fileInfo "UUID" "A48A45CA-46EE-233B-99BC-8987CE230E8F";
createNode transform -n "cube";
	rename -uid "309A57AB-48DA-615F-1598-3C9F8EE54529";
	setAttr ".rp" -type "double3" 0.5 0.5 0.5 ;
	setAttr ".sp" -type "double3" 0.5 0.5 0.5 ;
createNode nurbsCurve -n "curveShape4" -p "cube";
	rename -uid "4043BDE7-4127-29AE-92AC-E5ADBA597550";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		1 1 0
		1 1 1
		1 0 1
		1 0 0
		1 1 0
		;
createNode nurbsCurve -n "curveShape1" -p "cube";
	rename -uid "93E2BA91-4E04-AB10-728C-0586C8C306B0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		0 0 0
		0 0 1
		1 0 1
		1 0 0
		0 0 0
		;
createNode nurbsCurve -n "curveShape3" -p "cube";
	rename -uid "81F3BE67-43B9-6A4C-4583-7C90AA5BEF25";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		0 1 0
		0 1 1
		0 0 1
		0 0 0
		0 1 0
		;
createNode nurbsCurve -n "curveShape2" -p "cube";
	rename -uid "3F7CC42B-4C76-F94B-DF9A-4E9FFC85B9A3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		0 1 0
		0 1 1
		1 1 1
		1 1 0
		0 1 0
		;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".ren" -type "string" "arnold";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".vtn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".vn" -type "string" "ACES 1.0 SDR-video";
	setAttr ".dn" -type "string" "sRGB";
	setAttr ".wsn" -type "string" "ACEScg";
	setAttr ".otn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".potn" -type "string" "ACES 1.0 SDR-video (sRGB)";
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
// End of cube.ma
