from src.physics.gravity import gravity_force
from src.physics.physical_body import PhysicalBody
from src.physics.vector_2d import Vector2D
from src.physics.constants import GRAVITY_CONSTANT

def test_gravity_force_calculation():

    earth = PhysicalBody(mass=1000, radius=10, position=Vector2D(0, 0), velocity=Vector2D(0, 0), acceleration=Vector2D(0, 0))
    rocket = PhysicalBody(mass=10, radius=1, position=Vector2D(0, 10), velocity=Vector2D(0, 0), acceleration=Vector2D(0, 0))

    force = gravity_force(rocket, earth)

    expected_magnitude = GRAVITY_CONSTANT * (1000 * 10) / 100

    assert force.magnitude() == expected_magnitude
    assert force.x == 0
    assert force.y < 0  

def test_gravity_force_zero_division():

    body_a = PhysicalBody(mass=100, radius=5, position=Vector2D(5, 5), velocity=Vector2D(0, 0), acceleration=Vector2D(0, 0))
    body_b = PhysicalBody(mass=50, radius=2, position=Vector2D(5, 5), velocity=Vector2D(0, 0), acceleration=Vector2D(0, 0))

    force = gravity_force(body_a, body_b)

    assert force.x == 0
    assert force.y == 0