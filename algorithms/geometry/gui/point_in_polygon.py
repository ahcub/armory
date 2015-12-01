"""
To use this example you must click left mouse button at least three times on the window that will show after start.
After third click you must see polygon with vertexes in positions that you clicked.
If you continue to click left mouse button you will see how polygon changes according to your input.

To stop input polygon vertexes press right mouse button.
This will switch input mode into dot mode.
This means that your left click will set position of dot.
You will see it after first click.

When polygon and dot are set. You will see True or False flag in the top-left corner of the window.
this is indicator of is point in polygon.


To clean all data simply press right mouse button again. (you will be in polygon input mode again).
"""

import sys

import pygame

from algorithms.geometry.point_in_polygon import point_in_polygon

pygame.init()

screen = pygame.display.set_mode((640, 480))

polygon = []
dot_pos = 0
polygon_input_mode = True

white = (255, 255, 255)

label_font = pygame.font.SysFont("monospace", 15)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if polygon_input_mode:
                    polygon.append(event.pos)
                else:
                    dot_pos = event.pos
            if event.button == 3:
                if not polygon_input_mode:
                    polygon = []
                    dot_pos = 0
                polygon_input_mode = not polygon_input_mode

    screen.fill((0, 0, 0))
    if len(polygon) > 2:
        pygame.draw.polygon(screen, white, polygon, 2)
    if dot_pos:
        pygame.draw.circle(screen, white, dot_pos, 2)
    if len(polygon) > 2 and dot_pos:
        label = label_font.render(str(point_in_polygon(dot_pos, polygon)), 1, (255, 255, 0))
        screen.blit(label, (10, 10))

    pygame.display.flip()
