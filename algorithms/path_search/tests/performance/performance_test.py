from timeit import timeit

from algorithms.path_search.bellman_ford import bellman_ford
from algorithms.path_search.wave import wave
from algorithms.path_search.tests.data import graphs


def test(func, *args, **kwargs):
    def timeit_callable():
        func(*args, **kwargs)

    execution_time = timeit(timeit_callable, number=1000)
    print(func.__name__, 'algorithm execution time:', execution_time)


test(wave, **graphs['ordered_unweighted'])
test(bellman_ford, **graphs['ordered_weighted'])
