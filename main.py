import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers= (updatable, drawable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)/1000)


    print("Starting Asteroids!")
    print(f"Screen width: 1280")
    print(f"Screen height: 720")

if __name__ == "__main__":
    main()
