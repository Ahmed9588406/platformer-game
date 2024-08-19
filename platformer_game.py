# Imports for the game
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile,join

# Setup
pygame.init() # initialize the pygame

# Title for the game
pygame.display.set_caption("Platformer")

BG_COLOR = (255,255,255)

WIDTH,HEIGHT = 1000, 800

FBS = 60
PLAYER_VEL = 5 # Player Speed

window = pygame.display.set_mode((WIDTH,HEIGHT))


def main(window):
    """ This creates a Clock object that helps control the frame rate of the game.
    The Clock object can be used to manage how fast your game runs by controlling the time between frames."""
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FBS) # # Limit the frame rate to 60 frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)