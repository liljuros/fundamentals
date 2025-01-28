# values = [0]
# try:
#     minimum = abs(values[0])
#     for value in values[1:]:
#         if abs(value) < minimum:
#             minimum = abs(value)
# except IndexError as ex:
#     print(f'Exception occured: {ex}')
#     minimum = 0
#
#
#
# print(f'Minimum is: {minimum}')

try:
    raise ValueError('This is a custom message')
except ValueError as ex:
    print(f'Error value error message: {ex}')




