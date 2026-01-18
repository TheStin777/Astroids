import pygame
import constants
from logger import log_state
from player import *
from asteroidfield import *
from asteroid import Asteroid
from logger import log_event
import sys

def main():
    pygame.init()
    VERSION = pygame.version.ver
    WIDTH = constants.SCREEN_WIDTH
    HEIGHT = constants.SCREEN_HEIGHT
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {WIDTH}")
    print(f"Screen height: {HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    player_x = WIDTH/2
    player_y = HEIGHT/2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(player_x, player_y)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid = AsteroidField()

    while True:
        
        log_state()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        screen.fill("black")
        updatable.update(dt)
        
        for thing in drawable:
            thing.draw(screen)
        
        for asteroid in asteroids:
             if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        
        pygame.display.flip()
        dt = (clock.tick(60))/1000
        


if __name__ == "__main__":
    main()
