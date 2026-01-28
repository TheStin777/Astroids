from circleshape import CircleShape
from constants import *
import pygame
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, shoot_sound=None):
        self.cooldown_timer = 0
        self.shoot_sound = shoot_sound  # Store it as an instance variable
        
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
    
    def update (self, dt):
        self.cooldown_timer -= dt
        
      
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # ?
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # ?
            self.rotate(+dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.wrap_position()
            
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self):
                                    
        
        
        if  self.cooldown_timer > 0:
            return 


        else:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

        
        if self.shoot_sound:
            self.shoot_sound.play()
       

        
