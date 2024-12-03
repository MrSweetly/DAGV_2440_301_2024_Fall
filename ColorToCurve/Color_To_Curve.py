######
## Color To Curve
######

import maya.cmds as cmds # type: ignore

def set_node_color(color):
    color_map = {
        "black": 1, "grey": 2, "red": 13, "blue": 6, "green": 14,
        "yellow": 17, "purple": 9, "white": 16
    }

    if isinstance(color, str):
        color = color_map.get(color.lower(), None)
        if color is None:
            cmds.error(f"Invalid color name '{color}'. Use a number between 0-31 or a valid color name.")
        # End of if
    # End of if

    if not isinstance(color, int) or not (0 <= color <= 31):
        cmds.error("Color value must be an integer between 0-31 or a valid color name.")
    # End of if

    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.error("No objects selected. Please select one or more objects to change their color.")
    # End of

    for obj in selected_objects:
        shapes = cmds.listRelatives(obj, shapes=True, fullPath=True) or []
        for shape in shapes:
            if not cmds.attributeQuery("overrideEnabled", node=shape, exists=True):
                continue
            # End of if
            
            cmds.setAttr(f"{shape}.overrideEnabled", True)
            cmds.setAttr(f"{shape}.overrideColor", color)
        # End of for
    
    print(f"Color set to {color} for all shape nodes of selected objects.")
    # End of for
# End of set_node_color

set_node_color("yellow")

# Note: you can put in a color's name {red} or a number {1}.