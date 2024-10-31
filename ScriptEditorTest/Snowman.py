import maya.cmds as cmds # type: ignore

# Parameters
brim_radius = 2
brim_height = 0.3
crown_radius = 1.5
crown_height = 2
arm_length = 5
arm_radius = 0.2
subdivisions = 18

# Snowman
# Create the body
cmds.polySphere(r=6, sx=subdivisions, sy=subdivisions, name="Belly")
cmds.move(0, 6, 0)

cmds.polySphere(r=4, sx=subdivisions, sy=subdivisions, name="Chest")
cmds.move(0, 14, 0)

cmds.polySphere(r=2, sx=subdivisions, sy=subdivisions, name="Head")
cmds.move(0, 19, 0)

# Create arms
# Left arm
cmds.polyCylinder(r=arm_radius, h=arm_length, sx=8, name="L_Arm")
cmds.move(4.6, 14, 1.8)
cmds.rotate(-31, -26, 54)

# Right arm
cmds.polyCylinder(r=arm_radius, h=arm_length, sx=8, name="R_Arm")
cmds.move(-4.6, 14, 1.8)
cmds.rotate(-31, 26, -54)

# Create the eyes
# Right eye
cmds.polySphere(r=0.4, sx=subdivisions, sy=subdivisions, name="R_Eye")
cmds.move(-0.6, 19.9, 1.5)

# Left eye
cmds.polySphere(r=0.4, sx=subdivisions, sy=subdivisions, name="L_Eye")
cmds.move(0.6, 19.9, 1.5)

# Create the nose
cmds.polyCone(r=0.5, h=2, sx=subdivisions, sy=subdivisions, name="Nose")
cmds.rotate(90, 0, 90)
cmds.move(0, 19.2, 2.5)

# Create the mouth
mouth_offset = 1.2
for i in range(-2, 3):
    cmds.polySphere(r=0.25, sx=subdivisions, sy=subdivisions, name="Mouth_Pt")
    y_pos = 18.5 + 0.1 * (i ** 2)
    cmds.move(i * 0.5, y_pos, 2 - abs(i) * 0.1)

# Add buttons on the chest
cmds.polySphere(r=0.6, sx=subdivisions, sy=subdivisions, name="Button1")
cmds.move(0, 16.67, 3)

cmds.polySphere(r=0.6, sx=subdivisions, sy=subdivisions, name="Button2")
cmds.move(0, 15.15, 3.7)

cmds.polySphere(r=0.6, sx=subdivisions, sy=subdivisions, name="Button3")
cmds.move(0, 13.4, 3.9)

# Hat
# Create the brim of the hat
cmds.polyCylinder(r=brim_radius, h=brim_height, sx=subdivisions, sy=1, name="Brim")
cmds.move(0, brim_height / 2, 0)

# Create the crown of the hat
cmds.polyCylinder(r=crown_radius, h=crown_height, sx=subdivisions, sy=1, name="Crown")
cmds.move(0, brim_height + (crown_height / 2), 0)

# Combine the brim and crown into a single mesh
cmds.select("Brim", "Crown")
cmds.polyUnite(ch=1, name="Hat")
cmds.rotate(-10, 0, 0)
cmds.move(0, 20.26, 0)