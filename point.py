import math

class Point:

    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x-coordinate must be numerical")
        self.__x = float(value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y-coordinate must be numerical")
        self.__y = float(value)

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("distance_to() expects a Point instance")
        return math.hypot(self.__x - other.__x, self.__y - other.__y)

    def __repr__(self):
        return f"Point(x={self.x:,2f}, y={self.y:,2f})"

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def __eq__(self, other):
        return (
            isinstance(other, Point)
            and math.isclose(self.x, other.x)
            and math.isclose(self.y, other.y)
        )
