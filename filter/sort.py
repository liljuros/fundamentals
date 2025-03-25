# def key_func(x):
#     return abs(x)
#
# #data = [-10, 6, 0, 3, 6]
# data = [2, -2, 1, -1]
# #print(sorted([key_func(x) for x in data]))
# print(sorted(data, key=key_func, reverse=True))

data = [1,-2, 3, -4, 5, -6]
print(max(data, key=abs))