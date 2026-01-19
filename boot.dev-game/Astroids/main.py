import pygame
import constants
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
import sys
from shot import Shot

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
    # Adding Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Setting up the groups that were added
    #Player GROUP
    Player.containers = (updatable, drawable)
    player = Player(player_x, player_y)

    #Asteroid GROUP
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid = AsteroidField()

    #Shots GROUP
    Shot.containers = (shots, updatable, drawable)
    

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
            
            for shot in shots:
                if asteroid.collides_with(shot):
                  log_event("asteroid_shot")
                  asteroid.split()
                  shot.kill()
        
        
           

        
        pygame.display.flip()
        dt = (clock.tick(60))/1000
        


if __name__ == "__main__":
    main()
