# suits = ["spades", "hearst", "diamonds", "clubs"]
# for suit in suits:
#
#     print(f"{suit[0].upper()} = {suit}")

# for i in range(2,11,2):
#     print(i)

m = [
    [0,1],
    [2,3,4,5,6],
    [7,8,9],
    [10]
    ]

for row_index in range(len(m)):
    for col_index in range(len(m[row_index])):
        print(f'[{row_index, col_index}] = {m[row_index][col_index]}')

