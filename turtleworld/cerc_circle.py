from swampy.TurtleWorld import *

import sys
import math
try:
    # import if Swampy is installed as package
    from swampy.TurtleWorld import *
except ImportError:
    # if that doesn't work, then import from PYTHONPATH
    from TurtleWorld import *

def printusage():
    print('Exiting due to incorrect arguments.')
    print('To use as script, enter:')
    print('"python mycircle.py radiusinteger angleinteger"')

def drawpolyline(turtle, n, length, angle):
    """Draws n line segments
    
    turtle: Turtle object to draw with
    n: number of line segments
    length: length of each segment
    angle: angle to turn in between each
    """
    for i in range(n):
        fd(turtle, length)
        lt(turtle, angle)    
    
def drawpolygon(turtle, n, sidelength):
    """Draw a polygon. returning to start location.
    
    turtle: Turtle object to draw with
    n: Number of sides
    sidelength: length of each sidelength
    """
    angle = 360 / n                     # swampy TurtleWorld uses degrees
    drawpolyline(turtle, n, sidelength, angle)
        

def drawarc(turtle, r, angle):
    """Use many straight lines to approximate an arc.
    turtle: the turtle object to draw with.
    r: the radius of the arc.
    angle: angle subtended by the arc, in degrees
    """
    arclength = math.tau * r * abs(angle) / 360
    numberofsides = max(int(arclength*2), 30)
    steplength = arclength / numberofsides
    stepangle = angle / numberofsides
    lt(turtle, stepangle/2)
    drawpolyline(turtle, numberofsides, steplength, stepangle)
    rt(turtle, stepangle/2)

def drawcircle(turtle, r):
    """Approximate a circle with many small lines.
    turtle: the Turtle object to use to draw the circle.
    r: the radius of the circle.
    yourmom: so boring she makes these kind of coding jokes.
    """
    
if __name__ == '__main__':
    try:
        usrradius = int(sys.argv[1])
    except IndexError:
        donothingitsfine = None
    try:
        usrangle = int(sys.argv[2])
    except IndexError:
        donothingitsfine = None
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = .002
    drawarc(bob, 10, 360)
    drawarc(bob, 30, 360)
    wait_for_user()