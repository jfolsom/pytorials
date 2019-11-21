# Conway's Game of Life
import random
import time
import copy
WIDTH = 60
HEIGHT = 20

#Create a list of list for the cells:
nextcells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
            #append a living cell
            column.append('#')
        else:
            #append a dead cell
            column.append(' ')
    nextcells.append(column)

while True:
    print('\n\n\n\n\n')
    currentcells = copy.deepcopy(nextcells)
    # Print currentcells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentcells[x][y], end='')
        print()          #print newline at end of row

    # Calculate the next step's cells based on the current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # '% WIDTH' ensures leftcoord is always between 0 and WIDTH - 1
            leftcoord = (x - 1) % WIDTH
            rightcoord = (x + 1) % WIDTH
            abovecoord = (y - 1) % HEIGHT
            belowcoord = (y + 1) % HEIGHT
            # Count number of living neighbors
            numbneighbors = 0
            if currentcells[leftcoord][abovecoord] == '#':
                numbneighbors += 1
            if currentcells[x][abovecoord] == '#':
                numbneighbors += 1
            if currentcells[rightcoord][abovecoord] == '#':
                numbneighbors += 1
            if currentcells[leftcoord][y] == '#':
                numbneighbors += 1
            if currentcells[rightcoord][y] == '#':
                numbneighbors += 1
            if currentcells[leftcoord][belowcoord] == '#':
                numbneighbors += 1
            if currentcells[x][belowcoord] == '#':
                numbneighbors += 1
            if currentcells[rightcoord][belowcoord] == '#':
                numbneighbors += 1
            if currentcells[x][y] == '#' and (numbneighbors == 2 or numbneighbors == 3):
                nextcells[x][y] = '#'
            elif currentcells[x][y] == ' ' and numbneighbors == 3:
                nextcells[x][y] = '#'
            else:
                nextcells[x][y] = ' '
    time.sleep(0.05)


