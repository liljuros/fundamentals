# s1 = """
# “'And' and 'or' are the basic operations of logic. Together with 'no' (the logical operation
# of negation) they are a complete set of basic logical operations — all other logical
# operations, no matter how complex, can be obtained by suitable combinations of these.”
# ― John von Neumann, The Computer and the Brain
# """
#
# s2 = """
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
# labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
# nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
# esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
# in culpa qui officia deserunt mollit anim id est laborum.
# """
#
# charcount = {}
# for c in s1:
#     if c.isalpha():
#         charcount[c] = charcount.get(c, 0) +1
#
# print(charcount)

# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'d': 100, 'e': 200, 'f': 300}
# d3 = {'f': 30, 'g': 40}
#
# keys = []
# items = []
#
# for d in (d1,d2,d3):
#     keys.extend(list(d.keys()))
#     items.extend(list(d.values()))
#
# # for k, i in d1.items():
# #     keys.append(k)
# #     items.append(i)
# #
# # for k, i in d2.items():
# #     keys.append(k)
# #     items.append(i)
# #
# # for k, i in d3.items():
# #     keys.append(k)
# #     items.append(i)
#
#
# print(keys)
# print(items)
grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}

exam = {
    'Eric': 99,
    'John': 100
}

for student in grades:
    grades[student].insert(0, exam.get(student))


print(grades)