import copy
from abc import ABC, abstractmethod


class IClonable(ABC):
    @abstractmethod
    def clone(self):
        pass


class Shape(IClonable, ABC):
    def __init__(self):
        self.id = None
        self.name = None

    @abstractmethod
    def draw(self):
        pass

    def clone(self):
        return copy.copy(self)


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Circle"

    def draw(self):
        print(f"Drawing a circle with id {self.id}")


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Rectangle"

    def draw(self):
        print(f"Drawing a rectangle with id {self.id}")


class Square(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Square"

    def draw(self):
        print(f"Drawing a square with id {self.id}")


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
cloned_rectangle.draw()
cloned_rectangle.id = 5
cloned_square.draw()
cloned_square.id = 6
circle.draw()



