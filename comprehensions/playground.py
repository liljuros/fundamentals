numbers = [1,2,3,4,5,6,7,8]

# sq = []
# for i in number:
#     sq.append(i ** 2)
# sq = [number ** 2 for number in numbers]
# print(sq)

# evens = []
# for number in numbers:
#     if number % 2 ==0:
#         evens.append(number)
evens = [number for number in numbers if number % 2 == 0]
print(evens)