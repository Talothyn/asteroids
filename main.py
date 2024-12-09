#Importing pygame to allow for use of the open-source pygame library
from constants import *
import pygame
from player import *
from asteroid import *
from asteroidfield import *
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    running = True
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    AsteroidField.containers = (updatables, )
    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    

    
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for updatable in updatables:
            updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000
if __name__ == "__main__":
    main()
