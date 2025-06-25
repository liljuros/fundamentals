import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if not(isinstance(value, float) or isinstance(value, int)):
            raise ValueError('radius must be a float or an int')
        if value < 0:
            raise ValueError('radius cannot be negative')
        self._radius = value
    @property
    def area(self):
        return math.pi * self.radius ** 2

c = Circle(-1)

print(c.radius)


