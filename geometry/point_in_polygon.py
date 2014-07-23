from geometry.point import classify
from geometry.constants import *


def point_in_polygon(p, polygon):
    parity = False
    for index, vertex in enumerate(polygon):
        edge = polygon[index - 1], vertex
        e_type = edge_type(p, edge)
        if e_type == TOUCHING:
            return BOUNDARY
        elif e_type == CROSSING:
            parity = not parity
    return parity


def edge_type(p, e):
    org = e[0]
    dest = e[1]
    p_type = classify(p, org, dest)

    if p_type == LEFT:
        return CROSSING if ((org[1] < p[1]) and (p[1] <= dest[1])) else INESSENTIAL
    elif p_type == RIGHT:
        return CROSSING if ((dest[1] < p[1]) and (p[1] <= org[1])) else INESSENTIAL
    elif p_type in [BETWEEN, ORIGIN, DESTINATION]:
        return TOUCHING

    return INESSENTIAL