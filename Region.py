__author__ = 'Kaike'

from math import *
import os

# verify if the point is in the region
def region(point):
    if point[0]+point[1] <= 1:
        return False
    if pow(point[0]-1.0,2)+pow(point[1],2) - 1 >= 0:
        return False
    if pow(point[0],2)+pow(point[1]-1.0,2) - 1 >= 0:
        return False
    return True

def region_rasterization(image, color):
    for x in range(200):
        for y in range(200):
            if region([x/200.0, y/200.0]):
                image.putpixel([x, 200 - (y+1)], color)
    image.show()
    image.save(os.getcwd()+"\Images\\region.png", "png")