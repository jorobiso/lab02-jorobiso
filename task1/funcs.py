import math

def f(x: float) -> float:
    return 7 * (x**2) + 2*x

def g(x: float, y: float) -> float:
    return (x**2) + (y**2)

def hypotenuse(a: float, b: float) -> float:
    return math.sqrt((a**2) + (b**2))

def is_positive(z: bool):
    return (z>=0)
