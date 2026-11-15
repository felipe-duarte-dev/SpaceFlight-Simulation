from math import sqrt

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_vector):
        return Vector2D(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector):
        return Vector2D(self.x - other_vector.x, self.y - other_vector.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalization(self):
        unit = self.magnitude()

        try:
            return Vector2D(self.x / unit, self.y / unit )
        except ZeroDivisionError:
            return Vector2D(0, 0)