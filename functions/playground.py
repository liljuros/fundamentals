# def add(a,b,c):
#     print(locals())
#     sum_ = a + b + c
#     print(locals())
#     return a +b +c
#
# print(add(1,2,3))
# f = add
# print(globals())
# from datetime import datetime
#
# def log(message):
#     curr_time = datetime.utcnow().isoformat()
#     print(f'{curr_time} - [{message}]')
#
# log('This is a log')

# def my_func(a,b, *args):
#     print(type(args))
#     print(a)
#     print(b)
#     print(args)
#
# my_func(1,2,)

# data = [
#     [10,20,30],
#     [100,200,300],
#     [1000,2000,3000]
# ]
#
# def process_data(data, item_sep=',', line_sep='\n'):
#     row_strings = [
#         item_sep.join(str(el) for el in row)
#         for row in data
#     ]
#     return line_sep.join(row_strings)
#
#     # for row in data:
#     #     row_str = item_sep.join(str(el) for el in row)
#     #     output += row_str + line_sep
#
#
#     return output
# print((process_data(data)))
# test_dict = {
#     'a':5, 'b':10, 'c':15
# }
# def test_func(**kwargs):
#     for element, item in kwargs.items():
#         print(element, item)
#
# test_func(kwargs=test_dict)

# def test_func(a,b, *args, c=10, d=15, **kwargs):
#     print(a)
#     print(b)
#     for i in range(len(args)):
#         print(args[i])
#     print(c)
#     print(d)
#     for key, item in kwargs.items():
#         print(f"key: {key}, value {item}")
#
# test_func(1,3,5,6,7, f=35, g=45)

# print(round(123456, -2))
# t = (1,3,5,2,8,6)
# print(sorted(t, reverse=True))
# data = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4
#
# }
# items = {item*2:value for (item, value) in data.items()}
# print(items)
# from pprint import pprint
# l1 = 'xyzh'
# l2 = [1,2,3,4,5,6]
# data = [(a, b) for a in l1 for b in l2]
# pprint(data)

# s = '3.14/4.15/6.7/8.9'
# print(float(s).split('/')[1])
# import math
#
# def quadratic_solution(a, b, c):
#     # Calculate one solution of the quadratic equation
#     solution = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
#     return round(solution, 2)
#
# print(quadratic_solution(1, -5, 8))
# import math
#
# def quadratic_solutions(a, b, c):
#     discriminant = b**2 - 4*a*c
#     if discriminant < 0:
#         return "No real solution"
#     else:
#         sol1 = (-b + math.sqrt(discriminant)) / (2*a)
#         sol2 = (-b - math.sqrt(discriminant)) / (2*a)
#         return round(sol1, 2), round(sol2, 2)
#
# print(quadratic_solutions(1, -5, -8))

def encrypt(s):
    return ''.join(chr(ord(c) + 10) for c in s)

def decrypt(s):
    return ''.join(chr(ord(c) - 10) for c in s)

print(decrypt('S}kkm*Xo\x81~yx'))