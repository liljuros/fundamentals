# for i in range(1,5):
#     for j in range(1,5):
#         print(f'{i} + {j} = {i + j}')
#     print('-'*10)

# data = (
#     ['2021-01-01', 10, 20],
#     ['2021-01-02', 20, 18],
#     ['2021-01-03', -10, 10],
#     ['2021-01-04', 100, 102],
#     ['2021-01-05', 20, 45]
# )
# print(data)
# print("----"*10)
# for el in data:
#     el.append(abs(el[1])+abs(el[2]))
#
# largest = 0
# largest_date = ""
# for el in data:
#     if el[3] > largest:
#         largest = el[3]
#         largest_date = el[0]
# print(f"largest number is: {largest} on date {largest_date}")
#
#
# print(data)

data = [
    [10, 20],
    [20, 30],
    [35, 50],
    [45, 60]
]
previous = 0
first = True
for el in data:

    if not first:

        if el[0] == previous:
            el.append("same")

        elif el[0] > previous:
            el.append("down")

        else:
            el.append("up")
    else:
        el.append('')

    previous = el[1]



    first = False

print(data)