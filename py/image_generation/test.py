import bpy
import math
import time
from random import randint
from numpy import linspace

#get necessary stuff, name accordingly
scene = bpy.context.scene
camera_axis = bpy.data.objects["CameraAxis"]
camera = bpy.data.objects["Camera"]
material = bpy.data.materials["21:::"]

#set to default position
camera_axis.location = [0,0,0]
camera.location = [7,0,0]
camera_axis.rotation_euler = [0,0,0]
camera.rotation_euler = [math.pi / 2, 0, math.pi/2]

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

#small confirmation in case of wanting to back out
print("Press enter to continue or CTRL+C to exit")
_x = input()

#start timer
time_start = time.time()

#set colors to randomly choose from
colors = [
    [0.5, 0.5, 0.5, 1.0], #gray
    [1.0, 1.0, 1.0, 1.0], #white
    #[1.0, 1.0, 1.0, 0.7], #translucent, needs more work with material and rendering options
    [0.2, 0.2, 1.0, 1.0], #dark blue
    [1.0, 0.3, 1.0, 1.0], #pink
    [1.0, 0.1, 0.1, 1.0], #red
    [0.2, 1.0, 0.2, 1.0], #green
    [0.3, 0.4, 1.0, 1.0], #sky blue
    [0.1, 0.9, 1.0, 1.0], #cyan
    [0.2, 1.0, 0.2, 1.0], #light green
]

#render
for vertical_pos in range(vertical_steps):
    for horizontal_pos in range(horizontal_steps):        
        #rotate axis which has camera as child object
        camera_axis.rotation_euler = [0, vertical_degree_steps[vertical_pos], horizontal_degree_steps[horizontal_pos]]
        
        #set color randomly
        i = randint(0, len(colors)-1)
        material.diffuse_color = colors[i]
        
        #set render path as to not overwrite, then render it
        scene.render.filepath = image_path + "3037_" + str(vertical_pos) + "_" + str(horizontal_pos)
        bpy.ops.render.render(write_still = True)

print("My Script Finished: %.4f sec" % (time.time() - time_start))