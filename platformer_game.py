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
def get_background(name):
    image = pygame.image.load(join("assets","Background",name))
    _,_,width,height = image.get_rect() #* return x and y width and height i don't care about x and y
    tiles = []
        
    #! Adding one just in case i have a gape here
    #* Making sure that this will place in every tile of the screen
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            """Think of the screen like a big grid, similar to a checkerboard. Each square on this grid is a space where one of your background pictures (tiles) will go.
                i is like the column number on this grid.
                j is like the row number on this grid.
                width is how wide each tile is.
                height is how tall each tile is.
            """
            pos = (i * width,j*height)
            tiles.append(pos)
    return tiles,image

"""window: This is the game window where everything is displayed. It's like the canvas where you’re painting your game.
   background: This is a list containing the positions of all the tiles. Each position tells where a tile should go on the screen.
   bg_image: This is the image of the background tile that you want to draw."""

def draw(window,background,bg_image):
    for tile in background:
        window.blit(bg_image,tile)

    pygame.display.update()

def get_background(name):
    image = pygame.image.load(join("assets","Background",name))
    _,_,width,height = image.get_rect()

def main(window):
    """ This creates a Clock object that helps control the frame rate of the game.
    The Clock object can be used to manage how fast your game runs by controlling the time between frames."""
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FBS) # # Limit the frame rate to 60 frames per second
        background,bg_image = get_background("Blue.png")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window,background,bg_image)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)