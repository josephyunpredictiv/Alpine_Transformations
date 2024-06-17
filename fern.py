# -*- coding: utf-8 -*-
"""fern.ipynb
Original file is located at
    https://colab.research.google.com/drive/1Ugmk1G37638BUlzk33U1YX7MVfvM_mZ7
"""

import matplotlib.pyplot as plt
import numpy as np
import random

"""# Barnsley Fern and variants
### This link is better: https://www.chradams.co.uk/fern/maker.html
"""

# Given a matrix in the string as formatted in m_string, it returns a barnsley fern with alpine transformations
# Wiki: https://en.wikipedia.org/wiki/Barnsley_fern

n=1000000
name="Barnsley's"
scalar=1
save_fig=False
m_string="""
   0      0      0    .16     0      0    .01
  .85   .04   -.04    .85     0    1.6    .85
  .2   -.26    .23    .22     0    1.6    .07
 -.15   .28    .26    .24     0     .44   .07
"""

lines = [line.strip() for line in m_string.split("\n") if line.strip()]
matrix = [[float(elem) for elem in line.split(" ") if elem] for line in lines]

def transformation_1(p, matrix):
    x = p[0]
    y = p[1]
    x1 = matrix[0][0]*x + matrix[0][1]*y + matrix[0][4]
    y1 = matrix[0][2]*x + matrix[0][3]*y + matrix[0][5]
    return x1, y1

def transformation_2(p, matrix):
    x = p[0]
    y = p[1]
    x1 = matrix[1][0]*x + matrix[1][1]*y + matrix[1][4]
    y1 = matrix[1][2]*x + matrix[1][3]*y + matrix[1][5]
    return x1, y1

def transformation_3(p, matrix):
    x = p[0]
    y = p[1]
    x1 = matrix[2][0]*x + matrix[2][1]*y + matrix[2][4]
    y1 = matrix[2][2]*x + matrix[2][3]*y + matrix[2][5]
    return x1, y1

def transformation_4(p, matrix):
    x = p[0]
    y = p[1]
    x1 = matrix[3][0]*x + matrix[3][1]*y + matrix[3][4]
    y1 = matrix[3][2]*x + matrix[3][3]*y + matrix[3][5]
    return x1, y1

def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability)-1

def transform(p, matrix):
    transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
    probability = [matrix[0][6], matrix[1][6], matrix[2][6], matrix[3][6]]
    tindex = get_index(probability)
    t = transformations[tindex]
    x, y = t(p, matrix)
    return x, y

def draw_fern(n, matrix):
    x = [0]
    y = [0]

    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform((x1, y1), matrix)
        x.append(x1)
        y.append(y1)
    return x, y

x, y = draw_fern(n, matrix)
plt.figure(figsize=((max(x) - min(x))*scalar, (max(y) - min(y))*scalar))
plt.plot(x, y, '^', markersize=0.01, color='green')
plt.title('{0} Fern with {1} points'.format(name, n))
if save_fig:
    plt.savefig('fern.png', dpi=300)
plt.show()




# Code to create your own variants
n=1000000
name="Barnsley"
scalar=1
save_fig=False
m_string="""
   0      0      0    .16     0      0    .01
  .85   .04   -.04    .85     0    1.6    .85
  .2   -.26    .23    .22     0    1.6    .07
 -.15   .28    .26    .24     0     .44   .07
"""

lines = [line.strip() for line in m_string.split("\n") if line.strip()]
matrix = [[float(elem) for elem in line.split(" ") if elem] for line in lines]

x, y = draw_fern(n, matrix)
plt.figure(figsize=((max(x) - min(x))*scalar, (max(y) - min(y))*scalar))
plt.plot(x, y, '^', markersize=0.01, color='green')
plt.title('{0} Fern with {1} points'.format(name, n))
if save_fig:
    plt.savefig('fern.png', dpi=300)
plt.show()


# Culcita (=Calochlaenia) dubia
n=5000000
name="Culcita (=Calochlaenia) dubia:"
scalar=1
save_fig=False
m_string="""
  0     0     0    .25     0    -.14    .02
  .85    .02  -.02  .83     0     1      .84
  .09   -.28   .3   .11     0     .6     .07
 -.09    .28   .3   .09     0     .7     .07
"""

lines = [line.strip() for line in m_string.split("\n") if line.strip()]
matrix = [[float(elem) for elem in line.split(" ") if elem] for line in lines]

x, y = draw_fern(n, matrix)
plt.figure(figsize=((max(x) - min(x))*scalar, (max(y) - min(y))*scalar))
plt.plot(x, y, '^', markersize=0.01, color='green')
plt.title('{0} Fern with {1} points'.format(name, n))
if save_fig:
    plt.savefig('fern.png', dpi=300)
plt.show()


# Pellaea x Nephrolepis
n=1000000
name="Pellaea x Nephrolepis"
scalar=1
save_fig=False
m_string="""
  0      0      0     .25     0    -.4    .02
  .95    .002  -.002  .93    -.002  .5    .84
  .035  -.11    .27   .01    -.05   .005  .07
 -.04    .11    .27   .01     .047  .06   .07
"""

lines = [line.strip() for line in m_string.split("\n") if line.strip()]
matrix = [[float(elem) for elem in line.split(" ") if elem] for line in lines]

x, y = draw_fern(n, matrix)
plt.figure(figsize=((max(x) - min(x))*scalar, (max(y) - min(y))*scalar))
plt.plot(x, y, '^', markersize=0.01, color='green')
plt.title('{0} Fern with {1} points'.format(name, n))
if save_fig:
    plt.savefig('fern.png', dpi=300)
plt.show()


# Cyclosorus
n=1000000
name="Cyclosorus"
scalar=1
save_fig=False
m_string="""
 0      0      0     .25     0    -.4    .02
  .95    .005  -.005  .93    -.002  .5    .84
  .035  -.2     .16   .04    -.09   .02   .07
 -.04    .2     .16   .04     .083  .12   .07
"""

lines = [line.strip() for line in m_string.split("\n") if line.strip()]
matrix = [[float(elem) for elem in line.split(" ") if elem] for line in lines]

x, y = draw_fern(n, matrix)
plt.figure(figsize=((max(x) - min(x))*scalar, (max(y) - min(y))*scalar))
plt.plot(x, y, '^', markersize=0.01, color='green')
plt.title('{0} Fern with {1} points'.format(name, n))
if save_fig:
    plt.savefig('fern.png', dpi=300)
plt.show()

# Leptosporangiate
n=1000000
name="Leptosporangiate"
scalar=1
save_fig=False
m_string="""
   0     0     0    .25     0    -.14    .02
  .85    .02  -.02  .83     0     1      .84
  .09   -.28   .3   .11     0     .6     .07
 -.09    .28   .3   .09     0     .7     .07
"""

lines = [line.strip() for line in m_string.split("\n") if line.strip()]
matrix = [[float(elem) for elem in line.split(" ") if elem] for line in lines]

x, y = draw_fern(n, matrix)
plt.figure(figsize=((max(x) - min(x))*scalar, (max(y) - min(y))*scalar))
plt.plot(x, y, '^', markersize=0.01, color='green')
plt.title('{0} Fern with {1} points'.format(name, n))
if save_fig:
    plt.savefig('fern.png', dpi=300)
plt.show()

# Mutated Barnsly
n=1000000
name="Mutated Barnsly"
scalar=1
save_fig=False
m_string="""
  0      0      0     .25     0    -.4    .02
  .95    .005  -.005  .93    -.002  .5    .84
  .035  -.2     .16   .04    -.09   .02   .07
 -.04    .2     .16   .04     .083  .12   .07
"""

lines = [line.strip() for line in m_string.split("\n") if line.strip()]
matrix = [[float(elem) for elem in line.split(" ") if elem] for line in lines]

x, y = draw_fern(n, matrix)
plt.figure(figsize=((max(x) - min(x))*scalar, (max(y) - min(y))*scalar))
plt.plot(x, y, '^', markersize=0.01, color='green')
plt.title('{0} Fern with {1} points'.format(name, n))
if save_fig:
    plt.savefig('fern.png', dpi=300)
plt.show()


# Fractal Tree
n=1000000
name="Fractal Tree"
scalar=20
save_fig=False

m_string="""
   0      0      0    .5     0      0    .05
  .42   -.42   .42    .42     0    .2    .4
  .42   .42    -.42    .42     0    .2    .4
 .1   .0    .0    .1     0     .2   .15
"""

lines = [line.strip() for line in m_string.split("\n") if line.strip()]
matrix = [[float(elem) for elem in line.split(" ") if elem] for line in lines]

x, y = draw_fern(n, matrix)
plt.figure(figsize=((max(x) - min(x))*scalar, (max(y) - min(y))*scalar))
plt.plot(x, y, '^', markersize=0.01, color='green')
plt.title('{0} Fern with {1} points'.format(name, n))
if save_fig:
    plt.savefig('fern.png', dpi=300)
plt.show()


# Non alpine transformations
def draw_branch(ax, x, y, length, angle, depth,shrink):
    """Draw a branch recursively."""
    if depth == 0:
        return

    # Calculate the end point of the branch
    end_x = x + length * np.cos(angle)
    end_y = y + length * np.sin(angle)

    # Draw the branch
    ax.plot([x, end_x], [y, end_y], color='brown', linewidth=0.25)

    # Recursive calls to draw smaller branches
    draw_branch(ax, end_x, end_y, length * shrink, angle + np.pi / 4, depth - 1, shrink)
    draw_branch(ax, end_x, end_y, length * shrink, angle - np.pi / 4, depth - 1, shrink)
    #draw_branch(ax, end_x, end_y, length * shrink, angle, depth - 1)

def draw_tree(length, depth, shrink):
    """Draw a fractal tree."""
    fig, ax = plt.subplots()

    # Starting point of the tree
    start_x = 0
    start_y = 0

    # Draw the trunk
    ax.plot([start_x, start_x], [start_y, start_y + length], color='brown', linewidth=0.25)

    # Recursive calls to draw branches
    draw_branch(ax, start_x, start_y + length, length * shrink, np.pi / 2, depth, shrink)

    ax.set_aspect('equal')
    ax.set_title('Fractal Tree')
    ax.axis('off')
    plt.figure(figsize=(5, 5))
    if save_fig:
      plt.savefig('fern.png', dpi=300)
    plt.show()

# Parameters
tree_length = 5  # Length of the trunk
depth = 15  # Fractal depth

# Draw the fractal tree
save_fig=False
draw_tree(tree_length, depth, 0.7)


# Fractal Flower
def draw_petal(ax, x, y, length, angle, depth):
    """Draw a petal recursively."""
    if depth == 0:
        return

    # Draw the main petal
    new_x = x + length * np.cos(angle)
    new_y = y + length * np.sin(angle)
    ax.plot([x, new_x], [y, new_y], color='r')

    # Recursive calls to draw smaller petals
    draw_petal(ax, new_x, new_y, length * 0.7, angle + np.pi / 6, depth - 1)
    draw_petal(ax, new_x, new_y, length * 0.7, angle - np.pi / 6, depth - 1)

def draw_flower(num_petals, petal_length, depth):
    """Draw a flower with fractal petals."""
    fig, ax = plt.subplots()
    theta = np.linspace(0, 2*np.pi, num_petals, endpoint=False)

    for angle in theta:
        draw_petal(ax, 0, 0, petal_length, angle, depth)

    ax.set_aspect('equal')
    ax.set_title('Fractal Flower')
    ax.axis('off')
    plt.show()

# Parameters
num_petals = 6  # Number of petals
petal_length = 1  # Length of petals
depth = 10  # Fractal depth

# Draw the fractal flower
draw_flower(num_petals, petal_length, depth)


# Fern with high quality output
def transformation_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.85*x + 0.04*y # change
    y1 = -0.04*x + 0.85*y + 1.6
    return x1, y1

def transformation_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.2*x - 0.26*y
    y1 = 0.23*x + 0.22*y + 1.6
    return x1, y1

def transformation_3(p):
    x = p[0]
    y = p[1]
    x1 = -0.15*x + 0.28*y
    y1 = 0.26*x + 0.24*y + 0.44
    return x1, y1

def transformation_4(p):
    x = p[0]
    y = p[1]
    x1 = 0
    y1 = 0.16*y
    return x1, y1

def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability)-1

def transform(p):
    # list of transformation functions
    transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
    probability = [0.8, 0.07, 0.07, 0.01] #[0.85, 0.07, 0.07, 0.01]
    # pick a random transformation function and call it
    tindex = get_index(probability)
    t = transformations[tindex]
    x, y = t(p)
    return x, y

def draw_fern(n):
    # We start with (0, 0)
    x = [0]
    y = [0]

    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x, y

#n = int(input('Enter the number of points in the Fern: '))
n=5000000
x, y = draw_fern(n)
plt.figure(figsize=(8, 20))
# plot the points with triangle markers
plt.plot(x, y, '^', markersize=0.25, markerfacecolor='green', markeredgewidth=0)
plt.title('Fern with {0} points'.format(n))
plt.savefig('fern.png', dpi=300)
plt.show()


# Black Spleenwort Fern
def transformation_1(p):
    x=p[0]
    y=p[1]
    x1=0
    y1=0.16*y
    return x1, y1

def transformation_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.85*x - 0.04*y
    y1 = -0.04*x + 0.85*y + 1.6
    return x1, y1

def transformation_3(p):
    x = p[0]
    y = p[1]
    x1 = 0.2*x - 0.26*y
    y1 = 0.23*x + 0.22*y+1.6
    return x1, y1

def transformation_4(p):
    x = p[0]
    y = p[1]
    x1 = -0.15*x+0.28*y
    y1 = 0.26*x+0.24*y+0.44
    return x1, y1

def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability)-1

def transform(p):
    # list of transformation functions
    transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
    probability = [0.01, 0.85, 0.07, 0.07]
    # pick a random transformation function and call it
    tindex = get_index(probability)
    t = transformations[tindex]
    x, y = t(p)
    return x, y

def draw_fern(n):
    # We start with (0, 0)
    x = [0]
    y = [0]

    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x, y

#n = int(input('Enter the number of points in the Fern: '))
n=1000000
x, y = draw_fern(n)
plt.figure(figsize=(8, 12))
# plot the points with triangle markers
plt.plot(x, y, '^', markersize=0.25, markerfacecolor='green', markeredgewidth=0)
plt.title('Fern with {0} points'.format(n))
#plt.savefig('fern.png', dpi=300)
plt.show()




#mandelbol set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2]))

def plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, cmap='hot'):
    d = draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(d[2], extent=(xmin, xmax, ymin, ymax), cmap=cmap)
    plt.show()

plot_mandelbrot(-2.0, 1.0, -1.5, 1.5, 1000, 1000, 1024)



# Partial Flake
def flake(ax, start, vector, depth):
    if depth == 0:
        ax.plot([start[0], start[0] + vector[0]], [start[1], start[1] + vector[1]], color='red', linewidth = 0.5)
        return

    vector13 = vector / 3
    vector23 = vector * 2 / 3

    # First point
    flake(ax, start, vector13, depth - 1)

    new_start1 = start + vector13
    # Rotated by 60
    rotated_vector1 = np.array([vector13[0] * np.cos(np.pi / 3) - vector13[1] * np.sin(np.pi / 3),
                         vector13[0] * np.sin(np.pi / 3) + vector13[1] * np.cos(np.pi / 3)])
    flake(ax, new_start1, rotated_vector1, depth - 1)

    new_start2= new_start1 + rotated_vector1
    # Rotated by -60
    rotated_vector2 = np.array([vector13[0] * np.cos(-np.pi / 3) - vector13[1] * np.sin(-np.pi / 3),
                         vector13[0] * np.sin(-np.pi / 3) + vector13[1] * np.cos(-np.pi / 3)])
    flake(ax, new_start2, rotated_vector2, depth - 1)

    new_start3 = new_start2 + rotated_vector2
    # Final point
    flake(ax, new_start3, vector13, depth - 1)

def draw_snowflake(x, y, a, b, depth, save_fig=False):
    fig, ax = plt.subplots()
    start = np.array([x, y])
    vector1 = np.array([a, b])
    flake(ax, start, vector1, depth)
    for angle in [np.pi * 2 / 3, np.pi * 4 / 3]:
        # Rotating the vectors at 120 and 240 degrees
        rotated_vector = np.array([vector1[0] * np.cos(angle) - vector1[1] * np.sin(angle),
                                   vector1[0] * np.sin(angle) + vector1[1] * np.cos(angle)])
        flake(ax, start, rotated_vector, depth)

    ax.set_aspect('equal')
    ax.axis('off')

    if save_fig:
        plt.savefig('snowflake.png', dpi=300)
    plt.show()

draw_snowflake(0, 0, 1, 0, 7)

