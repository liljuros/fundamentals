data = {'a': 1, 'b':2, 'c':3}
# for i in data.items():
#     print(i)

# d = {
#     'key 1': 1,
#     'key 2': 2,
#     3.14: 'pi'
#
# }
#
# # for k in d:
# #     print(d[k])
#
# for k,v in d.items():
#     print(k, ' ', v)
d = {
    'length': 10,
    'width': 20
}
# print(d.get('height', False))

d.update(data)
print(d)