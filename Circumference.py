__author__ = 'Kaike'

from PIL import Image
from math import *
from Bresenham import *


# implicit circumference rasterization
def implicit_rasterization(image, radius, center, color):
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
    image.save("implicit_circumference.png", "png")
    image.show()


# parametric circumference rasterization
def parametric_rasterizarion(image, radius, center, color):
    for t in range(0, 360, 1):
        # in a circumference, x = rcos(t) and y = rsin(t)
        # add coordinates center to change to image referential
        start = [center[0]+int(radius*cos(radians(t))), center[1]+int(radius*sin(radians(t)))]
        end = [center[0]+int(radius*cos(radians(t+5))), center[1]+int(radius*sin(radians(t+5)))]

        approximate(start, end, image, color)
    image.save("parametric_circumference.png", "png")
    image.show()

black_color = (0, 0, 0)
white_color = (255, 255, 255)
implicit_image = Image.new('RGB', (200, 200), black_color)
parametric_image = Image.new('RGB', (200, 200), black_color)
radius = 100
center = [100, 100]
implicit_rasterization(implicit_image, radius, center, white_color)
parametric_rasterizarion(parametric_image, radius, center, white_color)











