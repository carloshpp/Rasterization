__author__ = 'Kaike'

from PIL import Image
from math import *
from Bresenham import *

def curve(t):
    return [t*cos(t), t*sin(t)]

def translate(vec, origin):
    vec[0] += origin[0]
    vec[1] += origin[1]

# get the point in the curve, transform into integer and translate to the center
def format_point(param, center):
    point = curve(param)
    point = [int(point[0]), int(point[1])]
    translate(point, center)
    return point

def uniform_sample_with_bresenham(sample, center, image, color):
    for k in range(0, 1000, 1):
        start = format_point(k*sample, center)
        end = format_point(k*sample+sample, center)
        approximate(start,end, image, color)
    image.save("uniform_sample_bresenham.png", "png")
    image.show()

def uniform_sample(sample, center, image, color):
    for k in range(0, 1000, 1):
        start = format_point(k*sample, center)
        image.putpixel(start,color)
    image.save("uniform_sample.png", "png")
    image.show()


def adaptive_sample_with_bresenham(center, image, color):
    space = 0.0
    while space < 100:
        sample = 1.0/sqrt(pow(cos(space) - space*sin(space),2)+pow(sin(space) + space*cos(space),2))
        space += sample
        start = format_point(space, center)
        end = format_point(space+sample, center)
        approximate(start,end,image,color)
    image.save("adaptive_sample_with_bresenham.png", "png")
    image.show()


def adaptive_sample(center, image, color):
    space = 0.0
    while space < 100:
        sample = 1.0/sqrt(pow(cos(space) - space*sin(space),2)+pow(sin(space) + space*cos(space),2))
        space += sample
        start = format_point(space, center)
        image.putpixel(start, color)
    image.save("adaptive_sample.png", "png")
    image.show()