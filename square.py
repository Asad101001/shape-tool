from point import Point
from regular_python import RegularPolygon
import math


class Square(RegularPolygon):

    def __init__(self, center: Point = Point(0, 0), side=1, rotation=45):
        radius = side / math.sqrt(2)
        super().__init__(n=4, radius=radius, center=center, rotation=rotation)
        self.side = side

    def area(self):
        return self.side**2

    def __str__(self):
        return f"Square(side={self.side:.2f}, area={self.area():.2f}, perimeter={self.perimeter():.2f}))"
