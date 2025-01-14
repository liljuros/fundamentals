l = ['AAPL', 'AAPL', 'Aapl', 'aapl', 'MSFT']

l2 = []
for symbol in l:
    l2.append(symbol.casefold())

s1 = set(l2)
print(s1)


data = {
    'd1': {'a': 1, 'b': 2, 'c': 3},
    'd2': {'b': 20, 'c': 30, 'd': 40},
    'd3': {'d': 100, 'x': 200}
}

#dict_keys = data['d1'].keys() | data['d2'].keys() | data['d3'].keys()

dict_keys = set()

for d in data.values():
    dict_keys = dict_keys | d.keys()



print(dict_keys)

