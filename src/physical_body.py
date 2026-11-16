from .vector_2d import Vector2D

class PhysicalBody:

    def __init__(self, mass, radius, position, velocity, acceleration):
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def update_position(self, delta_time):
        self.velocity = self.velocity + (self.acceleration * delta_time)
        self.position = self.position + (self.velocity * delta_time)
        self.acceleration = Vector2D(0, 0)

    def apply_force(self, force_vector):
        resulting_acceleration = force_vector * (1 / self.mass)
        self.acceleration = self.acceleration + resulting_acceleration

    def check_collision(self, other_body):
        resulting_vector = self.position - other_body.position
        resulting_magnitude = resulting_vector.magnitude()
        radius_sum = self.radius + other_body.radius

        return radius_sum >= resulting_magnitude
