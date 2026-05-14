import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create object ot help track time
    pygame_clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield_object = AsteroidField()

    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # player_object.update(dt)
        updatable.update(dt)
        for thing in asteroids:
            if thing.collides_with(player_object):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for thing in asteroids:
            for shot_thing in shots:
                if thing.collides_with(shot_thing):
                    log_event("asteroid_shot")
                    thing.split()
                    shot_thing.kill()


        # player_object.draw(screen)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        # pygame_clock.tick(60) will pause the gameloop until 1/60th of a second has passed
        # will also return amount of time passed since last time it was called
        dt = pygame_clock.tick(60) / 1000
        # should print around 0.016 seconds i think
        # print(dt)

    pygame.quit()

if __name__ == "__main__":
    main()
