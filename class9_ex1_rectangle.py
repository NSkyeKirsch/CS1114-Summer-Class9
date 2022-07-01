import math
import class9_ex1_shape as shape


class Rectangle(shape.Shape):  # Child class
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1)  # call parent initializer, send x1 and y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return "X:{}  Y:{}    X2:{}  Y2:{}".format(self.x, self.y, self.x2, self.y2)

    def calc_area(self):
        return math.fabs(self.x - self.x2) * math.fabs(self.y - self.y2)