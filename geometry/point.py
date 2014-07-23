from math import sqrt

from geometry.constants import *


def classify(p0, p1, p2):
    a = subtract(p2, p1)
    b = subtract(p0, p1)
    sa = a[0] * b[1] - a[1] * b[0]

    if sa > 0:
        return LEFT
    if sa < 0:
        return RIGHT
    if (a[0] * b[0] < 0) or (a[1] * b[1] < 0):
        return BEHIND
    if length(a) < length(b):
        return BEYOND
    if p0 == p1:
        return ORIGIN
    if p0 == p2:
        return DESTINATION
    return BETWEEN


def subtract(p0, p1):
    return (p0[0] - p1[0]), (p0[1] - p1[1])


def length(p):
    return sqrt(p[0] ** 2 + p[1] ** 2)