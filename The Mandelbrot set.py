# Mandelbrot Set by Giocrom
# z = z^2 + c
from matplotlib import pyplot as plt
from math import sqrt


def initialize_graph(res):
    step = sqrt(res)        # spacing between points
    x_range = int(step * 3.5)       # number of points in each row
    y_range = int(step * 2)     # number of points in each column
    real = -2.5     # starting value of x axes
    imaginary = -1      # starting value of y axes

    # Initialising the "points_x" and "points_y list", row by row
    for y in range(y_range):
        for x in range(x_range):
            real += step / res      # weights the step based on the resolution
            points_x.append(real)
            points_y.append(imaginary)
            c_number = complex(real + (imaginary * 1j))
            c_list.append(c_number)
            x += 1
        y += 1
        imaginary += step / res
        real = -2.5


def mandelbrot():
    for i in range(number_of_points):
        print("%.2f%%" % float((100 * i) / number_of_points))       # completion percentage
        z0 = c_list[i]
        z = 0.0
        iteration = 0
        max_iteration = 100     # good values = [100..1000]

        # Check if the current z is part of the set
        while (abs(z * z) <= 4) and (iteration in range(max_iteration)):
            z = z * z + z0      # Mandelbrot set equation
            iteration += 1
        color.append(1 / (iteration + 1))       # More iterations = darker color (max iterations = part of the set)


resolution = int(90000)  # Has to be a perfect square
number_of_points = 7 * resolution       # number of the total points that will be calculated
points_x = []       # List of the real parts of the complex numbers
points_y = []       # List of the imaginary parts of the complex numbers
c_list = []     # List of the complex numbers
color = []      # List of the color values

# The "initialize_graph" function creates an array of complex numbers evenly spaced between x = [-2.5..1] , y = [-1..1]
initialize_graph(resolution)

# The "mandelbrot" function calculates for all the numbers initialized by "initialize_graph" if they are part of the set
# or not and attributes to each point a color value saved in the "color" list
mandelbrot()

# Showing the graph
plt.scatter(points_x, points_y, label="Imaginary Numbers", s=.1, c=color)
plt.xlabel('real axis')
plt.ylabel('imaginary axis')
plt.title('complex numbers')
plt.show()
