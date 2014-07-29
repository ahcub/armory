from unittest.case import TestCase

from path_search.bellman_ford import bellman_ford
from path_search.tests.data import graphs
from path_search.wave import wave


class TestPathSearch(TestCase):
    def test_wave(self):
        self.assertEqual(wave(**graphs['ordered_unweighted']), [3, 4, 8, 9])

    def test_bellman_ford(self):
        self.assertEqual(bellman_ford(**graphs['ordered_weighted']), [3, 4, 8, 9])