class Point:
    """Represents a two-dimensional point """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'"The coordinates of this point are": {self.x} , {self.y}"'

class Circle:
    """Represents a circle"""
    def __init__(self, center: Point, r: float):
        self.center = center
        self.r = r

    def __str__(self) -> str:
        return f'"The coordinates of the circle "'



