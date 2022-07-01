import class9_ex1_rectangle as rectangle


class Square(rectangle.Rectangle):
    def __init__(self, x, y, width, length):
        if width == length:
            super().__init__(x, y, x+length, y+length)
        else:
            raise ValueError("Sides are not equal.")
