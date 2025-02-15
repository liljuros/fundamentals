def add(a,b):
    return a + b

def greet(name):
    return f'Hello, {name}!'

#print(add(2,3), greet("John"))

def apply(func, *args):
    result = func(*args)
    return result

print(apply(greet, "Erik"))