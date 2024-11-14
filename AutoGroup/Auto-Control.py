#####
## Auto-Control
#####

import maya.cmds as cmds  # type: ignore

def create_control_and_group(joint):

    if "_" in joint:
        base_name = "_".join(joint.split("_")[:-1])  # removes suffix if present
    else:
        base_name = joint
    # End of if else
    
    control_name = f"{base_name}_Ctrl"
    group_name = f"{control_name}_Grp"

    control = cmds.circle(name=control_name, normal=[1, 0, 0], radius=1.0)[0]
    
    joint_translation = cmds.xform(joint, query=True, translation=True, worldSpace=True)
    joint_rotation = cmds.xform(joint, query=True, rotation=True, worldSpace=True)
    cmds.xform(control, worldSpace=True, translation=joint_translation)
    cmds.xform(control, worldSpace=True, rotation=joint_rotation)
    
    control_group = cmds.group(empty=True, name=group_name)
    cmds.xform(control_group, worldSpace=True, translation=joint_translation)
    cmds.xform(control_group, worldSpace=True, rotation=joint_rotation)
    
    cmds.parent(control, control_group)
    
    parent_joint = cmds.listRelatives(joint, parent=True)
    if parent_joint:
        parent_control_group = f"{'_'.join(parent_joint[0].split('_')[:-1])}_Ctrl_Grp"
        if cmds.objExists(parent_control_group):
            cmds.parent(control_group, parent_control_group)
        # End of if
    # End of if

    children = cmds.listRelatives(joint, children=True, type="joint")
    if children:
        for child in children:
            create_control_and_group(child)
        # End of for
    # End of if
# End of create_control_and_group

def create_controls_for_selected():
    selected_joints = cmds.ls(selection=True, type="joint")
    if not selected_joints:
        cmds.warning("No joints selected. Please select the root joint(s) of the hierarchy.")
        return
    # End of if
    
    for joint in selected_joints:
        create_control_and_group(joint)
    # End of for
# End of 

create_controls_for_selected()

# Note: Sometimes places the control for the COG vertically instead of horizontally.