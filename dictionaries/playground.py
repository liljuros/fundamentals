data = {
    'start': 100,
    'high': 110,
    'low': 95,
    'closing': 105
}

# print('smurf' in data)
#
# l = [1,5,10,15]

d = dict.fromkeys(['open', 'high', 'low', 'close'], 0)

for key, item in d.items():
    print(key, item)
#print(d)