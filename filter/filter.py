data = list(range(1,11))

# def is_evens(n):
#     return n %2 == 0

# evens = (n for n in data if is_evens(n))
#
# #evens = (n for n in data if is_evens(data))
#
# print(list(evens))
# print(list(evens))

#evens = filter(is_evens, data)

evens = filter(lambda n: n % 2== 0, data)

print(list(evens))