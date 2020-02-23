#! python3
#  Setup cartesian axis to use in figuring out geometry of petal designs

import math
import time

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
    
from cerc_circle import *

def drawaxis(turtle, color, length, tick_length):
    """Draw one branch of an axis in the direction the turtle is currently
    facing.
    turtle = Turtle object.
    color = color to use for axis, as a string, e.g. 'blue', 'light blue'
    length = total length of axis.  Should be a multiple of tick_length
    tick_length = length of each tick.
    """
    turtle.set_pen_color(color)
    for i in range(length//tick_length):
        fd(turtle, tick_length)
        lt(turtle, 90)
        turtle.step()
        lt(turtle, 180)
        turtle.step()
        lt(turtle, 90)
    turtlehome(turtle)
   
def turtlehome(turtle):
    """Rest the turtle to the default starting position and color.
    Does not rest turtle.delay.
    """
    currentheading = turtle.get_heading()
    xposition = turtle.get_x()
    yposition = turtle.get_y()
    turtle.pu()
    rt(turtle, currentheading)
    fd(turtle, -1*xposition)
    lt(turtle, 90)
    fd(turtle, -1*yposition)
    rt(turtle, 90)
    turtle.set_pen_color('black')
    turtle.pd()

def drawradiants(turtle, color, length, tick_length):
    for i in range(0, 360, 15):
        lt(turtle, i)
        drawaxis(turtle, color, length, tick_length)

def drawaxes(turtle, color, length, tick_length):
    for i in [0, 90, 180, 270]:
        lt(turtle, i)
        drawaxis(turtle, color, length, tick_length)

def drawbutthole():
    world = TurtleWorld()    
    bob = Turtle()
    bob.delay = 0.01
    drawradiants(bob, 'light gray', 100, 100)
    drawaxes(bob, 'gray', 100, 20)


main()

# Script currently draws one branch then returns home.  to do:
# Draw four more branches.
# Draw anglelines in 15 degree increments (is light gray a color?)
# Import cerc_circle
# draw first two arcs
