from unittest.case import TestCase

from geometry import point
from geometry.constants import *


class TestPoint(TestCase):
    def test_classify(self):
        points_test_data = {
            ((1, 2), (1, 1), (3, 3)): LEFT,
            ((6, 2.5), (1, 1), (3, 3)): RIGHT,
            ((0, 0), (1, 1), (3, 3)): BEHIND,
            ((4, 4), (1, 1), (3, 3)): BEYOND,
            ((1, 1), (1, 1), (3, 3)): ORIGIN,
            ((3, 3), (1, 1), (3, 3)): DESTINATION,
            ((2, 2), (1, 1), (3, 3)): BETWEEN,
        }

        for input_data, expected_result in points_test_data.items():
            self.assertEqual(point.classify(*input_data), expected_result)

    def test_subtract(self):
        points_test_data = {
            ((5, 1), (4, 9)): (1, -8),
            ((2, 6), (1, 3)): (1, 3),
            ((10, 7), (4, 6)): (6, 1),
            ((23415123, 12612461), (12696754, 45793)): (10718369, 12566668),
        }
        for input_data, expected_result in points_test_data.items():
            self.assertEqual(point.subtract(*input_data), expected_result)

    def test_length(self):
        points_test_data = {
            (5, 0): 5,
            (1, 1): 1.4142135623730951,
            (0, 4): 4,
        }

        for input_data, expected_result in points_test_data.items():
            self.assertEqual(point.length(input_data), expected_result)