from timeit import timeit
from path_search.performance_tests.test_data import *
from path_search.wave import wave


def test(func, args):
    def timeit_callable():
        func(*args)
    execution_time = timeit(timeit_callable, number=1000)
    print(func.__name__, ' execution time:', execution_time)


test(wave, (test_graph_data, start, end))