import pygame
import constants

def main():
    VERSION = pygame.version.ver
    WIDTH = constants.SCREEN_WIDTH
    HEIGHT = constants.SCREEN_HEIGHT
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width:{WIDTH}")
    print(f"Screen height:{HEIGHT}")


if __name__ == "__main__":
    main()
