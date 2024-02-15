# https://www.geeksforgeeks.org/abstract-classes-in-python/
# Abstract Base Class (ABC)
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
# --------------------------------------------
class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have three sidex")

class Pentagon(Polygon):
    def noofsides(self):
        print("I have five sides")

class Hexagon(Polygon):
    def noofsides(self):
        print("I have six sides")

# Driver code
tri = Triangle()
tri.noofsides()

pen = Pentagon()
pen.noofsides()

hex = Hexagon()
hex.noofsides()
