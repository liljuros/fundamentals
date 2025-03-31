# import time
# def wrapper(func):
#     def inner(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         elapsed = end - start
#         print(f"Time taken: {elapsed:.6f} seconds")
#         return result
#     return inner
#
# @wrapper
# def add(a,b,c):
#     return a + b + c
#
# print(add(1,2,3))

# from decimal import Decimal
#
# PRECISION = 0
def normalize(PRECISION=2):
    def decorator(func):
        def inner(*args, **kwargs):
                result = func(*args, **kwargs)
                rounded_number = round(float(result), PRECISION)
                return rounded_number
        return inner
    return decorator
#
@normalize(8)
def perc_diff(x, y):
    try:
        return (y - x) / x * 100
    except ZeroDivisionError:
        return 0
#
@normalize(6)
def sum_squares(*args):
    return sum(x ** 2 for x in args)

@normalize(10)
def avg(*args):
    if len(args) == 0:
        return 0

    numbers = [Decimal(x) for x in args]
    sum_ = sum(numbers)
    return sum_ / len(numbers)

print(sum_squares(2,4))

from functools import lru_cache
# import time
# from timeit import timeit
# from time import sleep
#
# #@lru_cache()
# def add(x, y):
#     start = time.perf_counter()
#     sleep(2)
#     end = time.perf_counter()
#     print(end-start)
#     return x + y
#
# timeit('add(2, 2)', globals=globals(), number=10)