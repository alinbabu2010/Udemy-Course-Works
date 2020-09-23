# Abstraction in Python #
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):

    def __init__(self, side):
        self.__side = side
    
    def area(self):
        return self.__side * self.__side
        
    def perimeter(self):
        return 4 * self.__side


#myShape = Shape()       

mySquare = Square(5)
print("Area of square is", mySquare.area())
print("Perimeter of square is",mySquare.perimeter())
