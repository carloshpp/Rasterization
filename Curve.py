__author__ = 'Kaike'

from math import *
import os


def format_point(point, image):
    x = 4.0*point[0]/image.size[0] - 2.0
    y = 4.0*point[1]/image.size[1] - 2.0
    return pow(y,2)-pow(x,3)+x


def curve_rasterization(image, color):
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            p1 = format_point([x, y], image)
            p2 = format_point([x+1, y], image)
            p3 = format_point([x,y+1], image)

            if p1*p2 <= 0:
                if abs(p1) < abs(p2):
                    image.putpixel((x, y), color)
                else:
                    image.putpixel((x+1, y), color)

            if p1*p3 <= 0:
                if abs(p2) < abs(p3):
                    image.putpixel((x, y), color)
                else:
                    image.putpixel((x, y+1), color)

            if p2*p3 <= 0:
                if abs(p2) < abs(p3):
                    image.putpixel((x+1, y), color)
                else:
                    image.putpixel((x, y+1), color)
    image.save(os.getcwd()+"\Images\curve.png", "png")
    image.show()

