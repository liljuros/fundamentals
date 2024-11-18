from copy import deepcopy
# t = ([1,2], 3)
# t2 = t *3
#
# print(t2)
# t[0][1] = 5
# print(t2)

# l = [1,2,3,4,5,6,7,8,9,10]
# l2 = l[:]
# print(l2)
# l2[0] = 100
# print(l)
# print(l2)
# del l2[0]
# print(l2)

# l = [10,20,3,40,50]
# l.append([100,200])
# print(l)
# l.insert(3,42)
# print(l)
# l.insert(2,[1,2,3,4])
# print(l)

#s = 'FfEeDdCcBbAa'

# s_lower = s.lower()
# s_sorted = ''.join(sorted(s_lower))
# print(s_sorted)
# print(s_sorted.upper())

# t1 = 1, 2, 3, 4, 5, 6
# t2 = 7, 8, 9, 10
# t3 = 11, 12, 13, 14, 15, 16, 17
# l1 = list(t1)
# l2 = list(t2)
# l3 = list(t3)
#
# l1[::2] = [0,0,0]
# l2[::2] = [0,0]
# l3[::2] = [0,0,0,0]

# m = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]
# # m[0][0] = 1
# # m[1][1] = 1
# # m[2][2] = 1
# # print(m)
# m2 = deepcopy(m)
# m2[0][0] = 1
# m2[1][1] = 1
# m2[2][2] = 1
# print(m)
# print(m2)
data = [
    (100, 'USD', 'EUR', 0.83),
    (100, 'USD', 'CAD', 1.27),
    (100, 'CAD', 'EUR', 0.65)
]
i = 0
while i < len(data):
    amount, currency, target_currency, exchange_rate = data[i]
    converted = amount * exchange_rate
    print(amount,currency, '=', converted, target_currency, sep=' ' )
    i +=1
