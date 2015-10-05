__author__ = 'Kaike'

from PIL import Image
from Circumference import *
from Helix import *
from Region import *
from Curve import *

black_color = (0, 0, 0)
white_color = (255, 255, 255)
implicit_image = Image.new('RGB', (200, 200), black_color)
implicit_image_bresenham = Image.new('RGB', (200, 200), black_color)
parametric_image = Image.new('RGB', (200, 200), black_color)
parametric_image_bresenham = Image.new('RGB', (200, 200), black_color)
uniform_image = Image.new('RGB', (200, 200), black_color)
uniform_image_bresenham = Image.new('RGB', (200, 200), black_color)
adaptive_image = Image.new('RGB', (200, 200), black_color)
adaptive_image_bresenham = Image.new('RGB', (200, 200), black_color)
region_image = Image.new('RGB', (200, 200), black_color)
curve_image = Image.new('RGB', (200, 200), black_color)
radius = 100
center = [100, 100]
tolerance = 0.5


#implicit_rasterization(implicit_image, radius, tolerance, center, white_color)
#implicit_rasterization_with_bresenham(implicit_image_bresenham, radius, center, white_color)
#parametric_rasterizarion(parametric_image, radius, center, white_color)
#parametric_rasterizarion_with_bresenham(parametric_image_bresenham, radius, center, white_color)
#uniform_sample(0.1, center, uniform_image, white_color)
#uniform_sample_with_bresenham(0.1, center, uniform_image_bresenham, white_color)
#adaptive_sample(center, adaptive_image, white_color)
#adaptive_sample_with_bresenham(center, adaptive_image_bresenham, white_color)
#region_rasterization(region_image, white_color)
curve_rasterization(curve_image, white_color)