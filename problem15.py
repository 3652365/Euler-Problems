#!/usr/bin/python

'''
Problem 15
Lattice paths
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20*20 grid?
'''

'''
1 = right
0 = down
'''
import math
a = math.factorial(4)
b = math.factorial(2) ** 2
print a
print b
print a // b


grid = {}
def routes(x, y):
    if grid.get((x, y), 0):
        return grid[(x,y)]
    elif x == 0 or y == 0:
        grid[(x,y)] = 1
        return 1
    else:
        grid[(x,y)] = routes(x-1,y) + routes(x,y-1)
        print grid
        return grid[(x,y)]

print grid
print(routes(2,2))
