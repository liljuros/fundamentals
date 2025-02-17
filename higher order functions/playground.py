# def add(a,b):
#     return a + b
#
# def greet(name):
#     return f'Hello, {name}!'
#
# #print(add(2,3), greet("John"))
#
# def apply(func, *args):
#     result = func(*args)
#     return result
#
# print(apply(greet, "Erik"))

# data = ['a', 'ab', 'abc', 'abcd']
# # lengths = [len(element) for element in data]
# lengths = map(len, data)
# print(list(lengths))

def outer(a, b):
    sum_ = a + b

    def inner():
        prod = a *b
        print(a, b, sum_, prod)
        return "you just called a closure!"

    return inner()

func = outer(2,3)
print(func)