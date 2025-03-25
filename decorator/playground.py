def wrapper(func):

    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} is the name of the game")
        return result
    return inner
@wrapper
def add(a,b,c):
    return a + b+ c
@wrapper
def greet(name):
    return f"hello {name}"

def join(data, *, item_sep=',', line_sep='\n'):
    return line_sep.join(
        [
            item_sep.join(str(item) for item in row)
            for row in data
        ]
    )
print(greet('erik'))
print(add(1,2,3))

