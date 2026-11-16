from .vector_2d import Vector2D
from .constants import GRAVITY_CONSTANT

def gravity_force(body_1, body_2):

    distance = body_2.position - body_1.position
    scalar_distance = distance.magnitude()

    try:
        gravity = GRAVITY_CONSTANT * ((body_1.mass * body_2.mass) / scalar_distance ** 2) 
    except ZeroDivisionError:
        return Vector2D(0, 0)

    return distance.normalization() * gravity
