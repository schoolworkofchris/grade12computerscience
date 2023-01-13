# Import required libraries
from block import *
import random

# Inherits from Block to create a block that can move when an instance is created
class GoodBlock(Block):
    def update(self):
        # Moves the block in a random direction at a speed between -3 and 3
        self.rect.x += random.randint(-3, 3)
        self.rect.y += random.randint(-3, 3)