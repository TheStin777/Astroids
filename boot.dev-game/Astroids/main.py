import pygame
import constants
from logger import log_state
from player import *

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
    player = Player(player_x, player_y)

    while True:
        
        log_state()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60))/1000
        


if __name__ == "__main__":
    main()
