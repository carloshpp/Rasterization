__author__ = 'Kaike'


# draw line between two points in a image
def approximate(start, end, image, color):
    if start[0] > end[0]:
        approximate(end, start, image, color)
        return
    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]
    slope = 1
    if delta_y < 0:
        delta_y = -delta_y
        slope = -slope

    d = 2*delta_y-delta_x
    y = start[1]

    for x in range(start[0], end[0], 1):
        if abs(x) < image.size[0] and abs(y) < image.size[1]:
            image.putpixel([x, y], color)
        d += 2*delta_y
        if d > 0:
            d -= 2*delta_x
            y += slope