import pygame, constants, player
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    #Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        #Totally Black Screen
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

        player.update(dt)

    pygame.quit()

if __name__ == "__main__":
    main()