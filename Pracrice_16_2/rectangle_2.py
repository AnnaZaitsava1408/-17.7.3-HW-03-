from rectangle1 import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

square_1 = Square(5)
square_2 = Square(10)

сircle_1 = Circle(2)
сircle_2 = Circle(3)

figures = [rect_1, rect_2, square_1, square_2, сircle_1, сircle_2]

for figur in figures:
    print(figur, figur.get_area())


