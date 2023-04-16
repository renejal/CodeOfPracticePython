import math
import sys


def foo():
    pass

    try:
        import multiprocessing

        print(multiprocessing.cpu_count())
    except ImportError:
        print(sys.version)
    return math.pi
