# Import required libraries
from block import *
import random

# Class inheriting the fundementals of a block and adding functionality to move the blocks down until they fall off the screen
# They are then repositioned to a random place at the top of the screen
class BadBlock(Block):
    def update(self):
        # Creates the falling effect
        self.rect.y += 1
        # Checks if block is off the screen
        if self.rect.y > 400:
            # Randomly sets a new location for the x and y coordinates
            self.rect.y = random.randint(-50, -25)
            self.rect.x = random.randint(0, 700)