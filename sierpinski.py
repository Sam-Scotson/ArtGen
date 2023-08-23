import numpy as np
from PIL import Image, ImageDraw

def sierpinski_triangle(p1, p2, p3, depth, image):
    if depth == 0:
        draw_triangle(p1, p2, p3, image)
    else:
        midpoint1 = (p1 + p2) / 2
        midpoint2 = (p2 + p3) / 2
        midpoint3 = (p1 + p3) / 2

        sierpinski_triangle(p1, midpoint1, midpoint3, depth - 1, image)
        sierpinski_triangle(midpoint1, p2, midpoint2, depth - 1, image)
        sierpinski_triangle(midpoint3, midpoint2, p3, depth - 1, image)

def sierpinski_carpet(x, y, size, depth, image):
    if depth == 0:
        draw_square(x, y, size, image)
    else:
        new_size = size // 3
        for dx in range(0, size, new_size):
            for dy in range(0, size, new_size):
                if dx // new_size == 1 and dy // new_size == 1:
                    continue
                sierpinski_carpet(x + dx, y + dy, new_size, depth - 1, image)

def draw_triangle(p1, p2, p3, image):
    vertices = [p1, p2, p3]
    vertices = [(int(v[0]), int(v[1])) for v in vertices]
    ImageDraw.Draw(image).polygon(vertices, outline=255, fill=None)

def draw_square(x, y, size, image):
    ImageDraw.Draw(image).rectangle([x, y, x + size, y + size], outline=255, fill=None)

# Configuration
image_width = 800
image_height = 800
depth = 4
fractal_type = "sierpinski_carpet"  # Change this to "sierpinski_triangle" or "sierpinski_carpet"

fractal_image = Image.new('L', (image_width, image_height), 0)

if fractal_type == "sierpinski_triangle":
    sierpinski_triangle((0, image_height), (image_width, image_height), (image_width // 2, 0), depth, fractal_image)
elif fractal_type == "sierpinski_carpet":
    sierpinski_carpet(0, 0, image_width, depth, fractal_image)

fractal_image.save(f'{fractal_type}_fractal.png')
fractal_image.show()