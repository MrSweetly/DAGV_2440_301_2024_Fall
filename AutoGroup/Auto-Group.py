#########
##### Auto-Group
#########

import maya.cmds as cmds # type: ignore

def create_group():
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.warning("No objects selected. Please select at least one control.")
        return
    # End of if

    
    for obj in selected_objects:
        obj_translation = cmds.xform(obj, query=True, translation=True, worldSpace=True)
        obj_rotation = cmds.xform(obj, query=True, rotation=True, worldSpace=True)
        
        group_name = obj + "_Grp"
        new_group = cmds.group(empty=True, name=group_name)
        
        cmds.xform(new_group, worldSpace=True, translation=obj_translation)
        cmds.xform(new_group, worldSpace=True, rotation=obj_rotation)
        
        cmds.parent(obj, new_group)
    # End of for
# End of create_control_groups

# Run function
create_group()