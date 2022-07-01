
import class9_ex1_shape as shape
# or use -> from class9_ex1_shape import Shape
import class9_ex1_rectangle as rectangle
import class9_ex1_circle as circle
import class9_ex1_square as square


def main():
#   my_shape = shape.Shape(5, 10)
#    print(my_shape, my_shape.get_coordinates())

    my_rect = rectangle.Rectangle(3, 3, 12, 9)
    print(my_rect, ',', my_rect.calc_area())

    my_circ = circle.Circle(12.456, 12, 0)
    print("Circle: ", my_circ, my_circ.calc_area())

    my_sqr = square.Square(3, 4, 5, 5)
    print("Square: ", my_sqr, my_sqr.calc_area())


if __name__ == "__main__":
    main()
