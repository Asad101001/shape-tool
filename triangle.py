from irregular_polygon import IrregularPolygon

class Triangle(IrregularPolygon):
    
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise ValueError ("A triangle can only have 3 vertices , duhh!!")
        super().__init__(vertices)
        
    def __str__(self) -> str:
        return f"Triangle with area={self.area():.2f}, perimeter={self.perimeter():.2f}"       