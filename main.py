__author__ = 'Kaike'

from PIL import Image
from Circumference import *
from Helix import *

black_color = (0, 0, 0)
white_color = (255, 255, 255)
implicit_image = Image.new('RGB', (200, 200), black_color)
parametric_image = Image.new('RGB', (200, 200), black_color)
uniform_image = Image.new('RGB', (200, 200), black_color)
radius = 100
center = [100, 100]
#implicit_rasterization(implicit_image, radius, center, white_color)
#parametric_rasterizarion(parametric_image, radius, center, white_color)
#uniform_sample(0.1, center, uniform_image, white_color)
#uniform_sample_with_bresenham(0.1, center, uniform_image, white_color)
#adaptive_sample(center, uniform_image, white_color)
#adaptive_sample_with_bresenham(center, uniform_image, white_color)