from shape_interface import ShapeInterface
from point import Point
import math


class Polygon(ShapeInterface):

    def __init__(self, vertices):
        self.vertices = [v if isinstance(v, Point) else Point(*v) for v in vertices]

    @property
    def n(self):
        return len(self.vertices)

    @property
    def sides(self):
        if self.n < 2:
            return []
        return [
            math.hypot(
                self.vertices[(i + 1) % self.n].y - self.vertices[i].y,
            )
            for i in range(self.n)
        ]

    def perimeter(self):
        return sum(self.sides)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with {self.n} sides"
