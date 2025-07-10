from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=self.position, radius=self.radius, width = 2)
    
    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocities = [
            self.velocity.rotate(angle) * 1.2,
            self.velocity.rotate(-angle) * 1.2
        ]
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        for vel in velocities:
            new_ast = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast.velocity = vel