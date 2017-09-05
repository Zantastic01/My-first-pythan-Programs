# This program contains functions that evalute formulas used in geometry
#
# Zan Jones
# September 01, 2017

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

# funtion calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def parallelogram_area(b, h):
    a = b * h
    return a


def trapezoid_area(b, h, A):
    a = A + b / 2 * h
    return a


def right_rectangular_prism_volume(w, h, l):
    v = w*h*l
    return v


def right_circular_cone_volume(r, h):
    v = math.pi * r**2 * (h/3)
    return v


def sphere_volume(r):
    v = (4/3) * math.pi * r**3
    return v


def right_rectangular_prism_area(w, h, l):
    a = 2 * ( w*l + h*l + h*w)
    return a


def sphere_area(r):
    a = 4* math.pi * r**2
    return a

def pythagorean_theorem(A,b):
    a = A**2 + b**2
    return a


# funtion calls
print(parallelogram_area(6,6))
print(trapezoid_area(3, 4, 2))
print(right_rectangular_prism_volume(2, 3, 4))
print(right_circular_cone_volume(6,6))
print(sphere_volume(6))
print(right_rectangular_prism_area(6,6,7))
print(sphere_area(6))
print(pythagorean_theorem(6,6))

