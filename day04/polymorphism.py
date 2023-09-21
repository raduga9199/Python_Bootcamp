from day03.abstractions2 import Shape, Square, Rectangle
from day03.encapsulations2 import Person

shape1: Shape = Square(5)
shape2: Shape = Rectangle(3, 4)


def display_area(shape: Shape):
    print(f'{shape.name}\' area is {shape.area()}')


display_area(shape1)
display_area(shape2)

person1 = Person('James', 35)