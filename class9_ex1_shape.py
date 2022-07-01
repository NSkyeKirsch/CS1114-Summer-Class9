from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "X:{}  Y:{}".format(self.x, self.y)

    def get_coordinates(self):  # Accessor - returns a tuple of the coordinates for my shape
        return self.x, self.y

    @abstractmethod
    def calc_area(self):
        raise NotImplementedError

    # if you want to be a shape, you need an area function!!!


