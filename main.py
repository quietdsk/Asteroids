# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers =(updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

       updatable.update(dt)

       for asteroid in asteroids:
           for bullet in shots:
               if asteroid.collision_check(bullet):
                   asteroid.split()
                   bullet.kill()
           if asteroid.collision_check(player):
               print("game over")
               sys.exit()
               
               

       screen.fill((0,0,0))

       for obj in drawable:
            obj.draw(screen)

       pygame.display.flip()

       dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()