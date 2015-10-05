__author__ = 'Kaike'

from math import *
from Bresenham import *
import os

# implicit circumference rasterization using bresenham
def implicit_rasterization_with_bresenham(image, radius, center, color):
    for x in range(-radius, radius, 1):
        # in a circumference y = sqrt(r^2-x^2)
        # add coordinates center to change to image referential
        positive_start = [x+center[0], int(sqrt(abs(pow(radius, 2)-pow(x, 2))))+center[1]]
        positive_end = [x+1+center[0], int(sqrt(abs(pow(radius, 2)-pow(x+1, 2))))+center[1]]

        # the case when y is negative
        negative_start = [x+center[0], -int(sqrt(abs(pow(radius, 2)-pow(x, 2))))+center[1]]
        negative_end = [x+1+center[0], -int(sqrt(abs(pow(radius, 2)-pow(x+1, 2))))+center[1]]

        approximate(positive_start, positive_end, image, color)
        approximate(negative_start, negative_end, image, color)
    image.save(os.getcwd()+"\Images\implicit_circumference_with_bresenham.png", "png")
    image.show()

# implicit circumference rasterization
def implicit_rasterization(image, radius, tolerance, center, color):
    for x in range(-radius, radius, 1):
        for y in range(-radius, radius, 1):
            if (radius-tolerance) < sqrt(pow(x, 2)+pow(y, 2)) < radius+tolerance:
                image.putpixel([x+center[0], y+center[1]], color)
    image.save(os.getcwd()+"\Images\implicit_circumference.png", "png")
    image.show()

# parametric circumference rasterization
def parametric_rasterizarion_with_bresenham(image, radius, center, color):
    for t in range(0, 360, 1):
        # in a circumference, x = rcos(t) and y = rsin(t)
        # add coordinates center to change to image referential
        start = [center[0]+int(radius*cos(radians(t))), center[1]+int(radius*sin(radians(t)))]
        end = [center[0]+int(radius*cos(radians(t+5))), center[1]+int(radius*sin(radians(t+5)))]

        approximate(start, end, image, color)
    image.save(os.getcwd()+"\Images\parametric_circumference_with_bresenham.png", "png")
    image.show()


# parametric circumference rasterization
def parametric_rasterizarion(image, radius, center, color):
    for t in range(0, 360, 1):
        # in a circumference, x = rcos(t) and y = rsin(t)
        # add coordinates center to change to image referential
        start = [center[0]+int(radius*cos(radians(t))), center[1]+int(radius*sin(radians(t)))]
        if int(radius*cos(radians(t))) < radius and radius*sin(radians(t)) < radius:
            image.putpixel(start, color)
    print os.getcwd()

    image.save(os.getcwd()+"\Images\parametric_circumference.png", "png")
    image.show()









