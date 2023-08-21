import time

import requests


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return wrapper


@time_it
def fetch_page():
    requests.get("http://www.baidu.com")


fetch_page()