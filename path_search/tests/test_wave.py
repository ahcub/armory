from unittest.case import TestCase

from path_search.wave import wave


class TestWave(TestCase):
    def test_wave(self):
        test_graph_data = {
            1: [4],
            2: [3],
            3: [2, 4, 7],
            4: [1, 3, 8],
            5: [3, 6],
            6: [5, 10],
            7: [3],
            8: [4, 9],
            9: [8, 10],
            10: [6, 9],
        }

        self.assertEqual(wave(test_graph_data, 3, 9), [3, 4, 8, 9])