import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def create_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    r1 = np.linspace(x_min, x_max, width)
    r2 = np.linspace(y_min, y_max, height)
    pixels = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            c = r1[i] + r2[j] * 1j
            pixels[i, j] = mandelbrot(c, max_iter)
    return pixels

def plot_fractal(fractal):
    plt.imshow(fractal.T, cmap='hot', extent=(-2.5, 1.5, -2, 2))
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.xlabel('Real (Re)')
    plt.ylabel('Imaginary (Im)')
    plt.show()

# Define the parameters for the fractal
width = 1000
height = 1000
x_min = -2.5
x_max = 1.5
y_min = -2
y_max = 2
max_iter = 100

# Generate the fractal
fractal = create_fractal(width, height, x_min, x_max, y_min, y_max, max_iter)

# Plot the fractal
plot_fractal(fractal)