from math import pi

# class Cirle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2

class Cirle:
    def __init__(self,center_x, center_y,radius):
        self.radius = radius
        self.center = center_x, center_y

    def area(self):
        return pi * self.radius ** 2

    def translate(self, x, y):
        self.center = (self.center[0] + x, self.center[1] + y)

    def scale(self, factor):
        self.radius = self.radius * factor




c = Cirle(0,0,2)
print(c.radius)
print(c.center)
c.translate(1,-1)
print(c.center)
c.scale(10)
print(c.radius)
print(c.area())