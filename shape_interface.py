from abc import ABC,abstractmethod
import math

class ShapeInterface(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass