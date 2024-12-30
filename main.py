import pygame
from pygame.display import update
from pygame.mixer_music import play
from asteroidfields import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, drawable, updateable)
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    print(len(updateable))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updateable:
            item.update(dt)
        for item in asteroids:
            collides = player.has_collision(item)
            if collides:
                print("GAME OVER")
                return

            for bullet in shots:
                destroyed = item.has_collision(bullet)
                if destroyed:
                    bullet.kill()
                    item.split()
        screen.fill(color=(0,0,0))
        for item in drawable:
            item.draw(screen)
        dt = clock.tick(60) / 1_000
        pygame.display.flip()

if __name__ == "__main__":
    main()
