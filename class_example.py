import math


class Point:
    def __init__(self, x, y): # 'def' to define method
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance_origin(self):
        return math.sqrt(self.x**2 + self.y**2)


p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(2, 2)
p4 = Point(3, 4)
print(p1)
print(p2)
print(p1 == p2)
print(p2 == p3)
print(p4.distance_origin())