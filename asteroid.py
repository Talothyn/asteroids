from circleshape import *
from constants import *
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
         pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius)
         
    def update(self, dt):
        self.position += (self.velocity * dt) 
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_v1 = self.velocity.rotate(random_angle)
            new_v2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x,self.position.y, new_radius)
            new_asteroid1.velocity = new_v1
            
            new_asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
            new_asteroid2.velocity = new_v2


        
