import cProfile
import pstats
from io import StringIO
import re

def profile(func):
    """A decorator that uses cProfile to profile a function"""
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        ret = func(*args, **kwargs)
        pr.disable()
        s = StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats()
        print(s.getvalue())
        return ret
    return wrapper

@profile
def loop(count):
    # result = []
    # space_pattern = re.compile(r" ")
    for i in range(count):
        # result.append(i)
        st = " faei jflaie fealeij f"
        # re.sub(r" ", "", st)
        # space_pattern.sub("", st)
        a = [x for x in range(100)]

loop(1000000)
