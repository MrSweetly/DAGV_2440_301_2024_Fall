#######
## Sequential Renamer
#######

import maya.cmds as cmds # type: ignore

def rename_joint(base_name):
    
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("No objects selected. Please select an object to rename.")
        return
    # End of if

    if "#" not in base_name:
        cmds.warning("The naming scheme must include '#' characters for numbering.")
        return
    # End of if

    num_placeholders = base_name.count("#")
    if num_placeholders < 1:
        cmds.warning("The naming scheme must include at least one '#' character.")
        return
    # End of if

    parts = base_name.partition("#" * num_placeholders)
    prefix = parts[0]
    suffix = parts[2]

    def rename_selected(obj, count):
        new_name = f"{prefix}{str(count).zfill(num_placeholders)}{suffix}"
        renamed_obj = cmds.rename(obj, new_name)
        return renamed_obj

    count = 1
    for obj in selected_objects:
        rename_selected(obj, count)
        count += 1
    # End of for

    print(f"Renamed selected objects using naming scheme '{base_name}'.")
    # End of rename_selected
# End of rename_joint

rename_joint("Spine_##_Joint")

# Note: Rename the joint what you want, but it needs a "#" in it.