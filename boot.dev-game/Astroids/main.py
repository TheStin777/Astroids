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
     
    explode_sound = pygame.mixer.Sound("asteroid_exp.mp3")
    end_game_sound =pygame.mixer.Sound("game-over_sound.mp3")
    shoot_sound = pygame.mixer.Sound("shoot_sound.mp3")
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
    player = Player(player_x, player_y, shoot_sound)
    

    #Asteroid GROUP
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid = AsteroidField()

    #Shots GROUP
    Shot.containers = (shots, updatable, drawable)
    shoot_sound = pygame.mixer.Sound("shoot_sound.mp3")

    #Add scoring system take 1
    score = 0    
    
    #Player Lives
    lives = constants.PLAYER_LIVES
    
    

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
               if lives > 0:
                   lives -= 1
                   player.position.x = WIDTH/2
                   player.position. y = HEIGHT/2
                   
               else:                    
                    log_event("player_hit")                    
                    print(f"Final Score: {score}")
                    print("Game over!")  
                    end_game_sound.play()
                    while pygame.mixer.get_busy():
                        pygame.time.delay(50)
                        pygame.event.pump()
                    sys.exit()

                    
            
            for shot in shots:
                
                if asteroid.collides_with(shot):
                  log_event("asteroid_shot")
                  explode_sound.play()
                  asteroid.split()
                  shot.kill()
                  score += 10
        
        
           
        #Renderign Score
        font = pygame.font.SysFont (None, 36)
        score_text = font.render(f"Your Score  : {score}", True, "white")
        screen.blit(score_text, (10, 10))

        #Rendering Lives

        font = pygame.font.SysFont (None, 36)
        score_text = font.render(f"Your lives  : {lives}", True, "white")
        screen.blit(score_text, (10, 40))

        pygame.display.flip()
        dt = (clock.tick(60))/1000
        


if __name__ == "__main__":
    main()
