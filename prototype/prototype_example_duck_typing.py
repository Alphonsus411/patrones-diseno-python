import copy


class Circle:
    def __init__(self):
        self.id = None
        self.name = "Circle"

    def draw(self):
        print(f"Drawing a circle with id {self.id}")

    def clone(self):
        return copy.copy(self)


class Rectangle:
    def __init__(self):
        self.id = None
        self.name = "Rectangle"

    def draw(self):
        print(f"Drawing a rectangle with id {self.id}")

    def clone(self):
        return copy.copy(self)


class Square:
    def __init__(self):
        self.id = None
        self.name = "Square"

    def draw(self):
        print(f"Drawing a square with id {self.id}")

    def clone(self):
        return copy.copy(self)


circle = Circle()
circle.id = 1
rectangle = Rectangle()
rectangle.id = 2
square = Square()
square.id = 3

circle.draw()
rectangle.draw()
square.draw()

cloned_circle = circle.clone()
cloned_rectangle = rectangle.clone()
cloned_square = square.clone()

cloned_circle.draw()
cloned_circle.id = 4
cloned_circle.draw()
cloned_rectangle.draw()
cloned_rectangle.id = 5
cloned_rectangle.draw()
cloned_square.draw()
cloned_square.id = 6
cloned_square.draw()
circle.draw()