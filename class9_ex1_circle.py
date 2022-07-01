import math
import class9_ex1_shape as shape


class Circle(shape.Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return super().__str__() + "   radius {:3.2f}".format(self.radius)

    def calc_area(self):
        return math.pi * self.radius ** 2
