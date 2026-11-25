from .gravity import gravity_force
from .physical_body import PhysicalBody


class PhysicsWorld:
    def __init__(self, bodies: list[PhysicalBody]):
        if len(bodies) not in (2, 3):
            raise ValueError("PhysicsWorld only supports 2 or 3 bodies.")

        self.bodies = bodies
        self.elapsed_time = 0.0
        self.collided = False

    def update_world(self, dt: float):
        if self.collided:
            return

        if len(self.bodies) == 2:
            earth, rocket = self.bodies
            rocket.apply_force(gravity_force(rocket, earth))

        elif len(self.bodies) == 3:
            earth, rocket, moon = self.bodies
            rocket.apply_force(gravity_force(rocket, earth))
            rocket.apply_force(gravity_force(rocket, moon))
            moon.apply_force(gravity_force(moon, earth))
            moon.apply_force(gravity_force(moon, rocket))

        for body in self.bodies:
            body.update_position(dt)

        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                if self.bodies[i].check_collision(self.bodies[j]):
                    self.collided = True

        self.elapsed_time += dt