# from math import pi
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
# c = Circle(1)
# print(c.area())
import csv

file_name = 'DEXUSEU.csv'

# with open(file_name) as f:
#     for _ in range(5):
#         print(next(f))

with open(file_name) as f:
    reader = csv.reader(f)
    headers = next(reader)
    data = list(reader)
    print(data)