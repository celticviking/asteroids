# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Asteroids")

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    #Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        #Totally Black Screen
        screen.fill((0,0,0))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()