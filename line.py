from point import Point


class Line:

    def __init__(self, start_point, end_point):
        if not all(isinstance(p, Point) for p in (start_point, end_point)):
            raise TypeError("Line endpoints must be Point instances")
        self.start = start_point
        self.end = end_point

    @property
    def length(self):
        return self.start.distance_to(self.end)

    def __eq__(self, other):
        return isinstance(other, Line) and (
            (self.start == other.start and self.end == other.end)
            or (self.start == other.end and self.end == other.start)
        )

    def __repr__(self):
        return f"Line(start={self.start}, end={self.end}, lenght={self.length:.2f})"
