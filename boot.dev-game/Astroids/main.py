import pygame
import constants
from logger import log_state

def main():
    pygame.init()
    VERSION = pygame.version.ver
    WIDTH = constants.SCREEN_WIDTH
    HEIGHT = constants.SCREEN_HEIGHT
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {WIDTH}")
    print(f"Screen height: {HEIGHT}")

    while log_state:
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
