from objects import *
import math


def distance(p_one: Point, p_two: Point) -> float:
    return (math.sqrt((c_two.center.x - c_one.center.x)**2 + (c_two.center.y - c_one.center.y)**2))


def circles_overlap(c_one: Circle, c_two: Circle) -> bool:
    return distance(c_one.center, c_two.center) < (c_one.r + c_two.r)


