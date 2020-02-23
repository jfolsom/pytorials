from cerc_circle import *

import sys
import math
import time

world = TurtleWorld()
bob = Turtle()
bob.delay=.002

numberofpetals = 3
petallength = 100
twixtpetals = 360/numberofpetals     # in degrees for turtleworld
petalarc = 30                        # also in degrees
parcradius = (petalarc*math.tau) / (24 * math.sin(math.radians(30)))


# orient for first turn, for three petals.
lt(bob, (twixtpetals - petalarc/2))

# draw first half of first petalarc
drawarc(bob, parcradius, petalarc)

time.sleep(2)
sys.exit()

