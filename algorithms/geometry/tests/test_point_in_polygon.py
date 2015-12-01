from unittest.case import TestCase

from algorithms.geometry import point_in_polygon
from algorithms.geometry.constants import *


class TestPointInPolygon(TestCase):
    def test_point_in_polygon(self):
        polygon_test_data = (
            (1, 2),
            (2, 7),
            (4, 8),
            (5, 7),
            (6, 5),
            (3, 3),
        )
        points_true_test_data = {
            (5, 5): True,
            (10, 5): False,
            (4.5, 7.5): BOUNDARY,
        }

        for input_data, expected_result in points_true_test_data.items():
            self.assertEqual(point_in_polygon.point_in_polygon(input_data, polygon_test_data), expected_result)

        points_false_test_data = {
            (20, 5): BOUNDARY,
            (4, 7): False,
            (1, 1): True,
        }
        for input_data, expected_result in points_false_test_data.items():
            self.assertNotEqual(point_in_polygon.point_in_polygon(input_data, polygon_test_data), expected_result)

    def test_edge_type(self):
        edge_test_data = ((4.5, 8), (7, 1))
        points_test_data = {
            (4.5, 8): TOUCHING,
            (2, 5): CROSSING,
            (1, 0): INESSENTIAL,
        }

        for input_data, expected_result in points_test_data.items():
            self.assertEqual(point_in_polygon.edge_type(input_data, edge_test_data), expected_result)
