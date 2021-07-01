import bpy
import math
import time
from numpy import linspace

#start timer
time_start = time.time()

#get necessary stuff
scene = bpy.context.scene
camera_axis = bpy.data.objects["Empty"]
camera = bpy.data.objects["Camera"]

#set to default position
camera_axis.location = [0,0,0]
camera.location = [5,0,0]
camera_axis.rotation_euler = [0,0,0]
camera.rotation_euler = [0,0,0]

#define number of steps
vertical_steps = 24
horizontal_steps = 64

#get steps in radians
vertical_degree_steps = linspace(-math.pi/2, math.pi/2, vertical_steps)
horizontal_degree_steps = linspace(0, math.pi * 2, horizontal_steps, endpoint=False)

print(len(vertical_degree_steps), " vertical stops")
print(vertical_degree_steps)
print()
print(len(horizontal_degree_steps), " horizontal stops")
print(horizontal_degree_steps)
print()
print(len(vertical_degree_steps) * len(horizontal_degree_steps), " total points")

#change accordingly
image_path = "C:/Users/Anto/Fakultetlije/semestar_dipl_4/dipl/archive/test/"

for vertical_pos in range(vertical_steps):
    for horizontal_pos in range(horizontal_steps):
        print(vertical_pos, horizontal_pos)
        #rotate axis which has camera as child object
        camera_axis.rotation_euler = [0, vertical_degree_steps[vertical_pos], horizontal_degree_steps[horizontal_pos]]
        #set render path as to not overwrite, then render it, rinse and repeat until the for loops are done
        scene.render.filepath = image_path + "test_" + str(vertical_pos) + "_" + str(horizontal_pos)
        bpy.ops.render.render(write_still = True)

print("My Script Finished: %.4f sec" % (time.time() - time_start))