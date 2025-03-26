import time
def wrapper(func):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Time taken: {elapsed:.6f} seconds")
        return result
    return inner

@wrapper
def add(a,b,c):
    return a + b + c

print(add(1,2,3))