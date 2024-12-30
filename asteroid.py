import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20,50)
        first = self.velocity.rotate(angle)
        second = self.velocity.rotate(-angle)
        rad = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, rad).velocity = first
        Asteroid(self.position.x, self.position.y, rad).velocity = second
