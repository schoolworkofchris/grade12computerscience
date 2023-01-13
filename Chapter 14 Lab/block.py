# Import required libraries
import pygame
from vars import *

# Central Block Class, this contains the fundemental functions and properties of any block
class Block(pygame.sprite.Sprite):
    def __init__(self, filename):
        # Call the parent class (Sprite) constructor
        super().__init__() 
 
        # Creates and image where filename can be substitubed with the name of the file
        self.image = pygame.image.load(filename).convert()
 
        # Sets a universal color key
        self.image.set_colorkey(BLACK)
 
        # Creates a rectangle around the image (you could call this a hit box)
        self.rect = self.image.get_rect()