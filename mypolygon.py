from swampy.TurtleWorld import *

import sys

usrlength = int(sys.argv[1])
usrsides = int(sys.argv[2])

world = TurtleWorld()
bob = Turtle()
print(bob)

def drawpoly(aturtle, length, sides):
    turnangle = 360 / sides
    for i in range(sides):
        fd(aturtle, length)
        lt(aturtle, turnangle)

drawpoly(bob, usrlength, usrsides)

wait_for_user()