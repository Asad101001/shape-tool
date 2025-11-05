from polygon import Polygon
from point import Point
import math


class RegularPolygon(Polygon):

    def __init__(self, n, radius, center: Point = Point(0, 0), rotation=0):
        if n < 3:
            raise ValueError("A polygon must have atleast 3 sides")
        self._num_sides = n
        self.radius = radius
        self.center = center if isinstance(center, Point) else Point(*center)
        self.rotation = math.radians(rotation)
        self.vertices = self.compute_vertices()
        super().__init__(self.vertices)

    def compute_vertices(self):
        cx, cy = self.center.x, self.center.y
        vertices = []
        angle_inc = 2 * math.pi / self.n
        angle = self.rotation

        for _ in range(self.n):
            x = cx + self.radius * math.cos(angle)
            y = cy + self.radius * math.sin(angle)
        return vertices

    def area(self):
        s = self.sides[0]
        n = self.n
        return (n * s**2) / (4 * math.tan(math.pi / n))
