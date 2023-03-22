from vpython import *
import time
import random

# set up the snowman
bottom = sphere(pos=vector(0, -1, 0), radius=2, color=color.white)
middle = sphere(pos=vector(0, 1, 0), radius=1.5, color=color.white)
top = sphere(pos=vector(0, 3, 0), radius=1, color=color.white)
hat = cone(pos=vector(0, 4, 0), axis=vector(0, 2, 0), radius=1, color=color.cyan)
left_arm = cylinder(pos=vector(-2, 1.5, 0), axis=vector(5, 0, 0), radius=0.1, color=vector(139/255, 69/255, 19/255))
right_arm = cylinder(pos=vector(2, 1.5, 0), axis=vector(-5, 0, 0), radius=0.1, color=vector(139/255, 69/255, 19/255))


# define the dance moves
def move_arms():
    for i in range(3):
        left_arm.rotate(angle=pi/6, axis=vector(0, 1, 0))
        right_arm.rotate(angle=-pi/6, axis=vector(0, 1, 0))
        time.sleep(0.1)
        left_arm.rotate(angle=-pi/6, axis=vector(0, 1, 0))
        right_arm.rotate(angle=pi/6, axis=vector(0, 1, 0))
        time.sleep(0.1)

def change_hat ():
    colors = [color.red, color.green, color.cyan, color.magenta, color.orange]
    for i in range(3):
        currentColor =  random.choice(colors)
        hat.color = currentColor
        time.sleep(0.1)




# make the snowman dance
while True:
    move_arms()
    change_hat()

