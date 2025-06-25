import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f'Circle(radius={self.radius})'

    def __eq__(self, other):
        return isinstance(other,Circle) and self.radius == other.radius



c1 = Circle(1)
c2 = Circle(1)

print(c1 == c2)