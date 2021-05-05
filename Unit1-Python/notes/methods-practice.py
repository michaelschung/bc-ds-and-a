'''
Mr. Chung
3/1: Methods Practice
'''

import math

# 1) Method that prints your name and your grade
def name_grade():
    print('Weezie, 11')

# 2) Method that takes a number as a parameter, and prints that number + 20
def add_nums(n):
    print(n + 20)

# 3) Function that takes three numbers as parameters, and returns the sum of the first two divided by the third
def triple(x, y, z):
    return (x + y) / z

# 4) Function that takes two parameters representing the base and height of a triangle, and returns the area of that triangle
def tri_area(b, h):
    return b * h / 2

# 5) Function that takes four parameters representing the coordinates of two points, and returns the distance between those points
def distance(x1, y1, x2, y2):
    xDiffSq = (x2 - x1)**2
    yDiffSq = (y2 - y1)**2
    return math.sqrt(xDiffSq + yDiffSq)

# 6) Function that takes parameters representing the coefficients of the terms of a quadratic equation in standard form, and prints the solutions to the quadratic equation
def quad(a, b, c):
    sqrtDet = math.sqrt(b**2 - 4 * a * c)
    first = -b / (2 * a)
    second = sqrtDet / (2 * a)
    print(first + second)
    print(first - second)

def quad2(a, b, c):
    sqrtDet = math.sqrt(b**2 - 4 * a * c)
    denom = 2 * a
    print ((-b + sqrtDet) / denom)
    print ((-b - sqrtDet) / denom)

quad2(1, 2, 1)   # -1, -1
quad2(1, 1, -6)  # -3, 2
quad2(2, -3, -2) # -0.5, 2









#
