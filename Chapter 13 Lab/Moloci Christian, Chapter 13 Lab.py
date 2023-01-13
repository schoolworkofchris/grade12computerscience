"""
Christian Moloci

Chapter 13 Lab
"""
import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (17, 148, 252)
GREEN = (124, 200, 20)
SKY = (194, 241, 251)
 
# Class for blocks, serves as a template for both good and bad blocks
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

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, filename, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Creates and image where filename can be substitubed with the name of the file
        self.image = pygame.image.load(filename).convert()
 
        # Sets a universal color key
        self.image.set_colorkey(BLACK)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
# Initialize Pygame
pygame.init()
 
# Set screen properties such as dimensions and text
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Chris's Mario Game Rip Off")

# Load in all of our sounds so we can use them
good_sound = pygame.mixer.Sound("coin.wav")
bad_sound = pygame.mixer.Sound("damage.wav")
wall = pygame.mixer.Sound("wall.wav")

# Handles the loading and playing of the theme song
pygame.mixer.music.load("song.wav")
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# Loof to create 50 good hit boxes with the coin sprit set to them (uses block class as template)
for i in range(50):
    # This represents a block
    block = Block("coin.png")
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)

# Loop to create 50 bad hit boxes with the goomba sprite set to them (uses block class as template)
for i in range(50):
    # This represents a block
    block = Block("goomba.png")
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    bad_block_list.add(block)
    all_sprites_list.add(block)
 
# Create a RED player block
player = Player("mario.png", 0, 0)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Set a variable to keep track of our score
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

        #  if stateements to see which was the user want to go (or not go) when pressing (or not pressing) the arrow keys
        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
    
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
 
    # Clear the screen
    screen.fill(SKY)

    # Load in a font to display the score later
    font = pygame.font.SysFont('Comic Sans MS', 25, True, False)

    # Wall collision handlers
    if player.rect.x <= -12:
        player.rect.x = -11
        wall.play()
    if player.rect.x >= 662:
        player.rect.x = 661
        wall.play()

    if player.rect.y <= -2:
        player.rect.y = -1
        wall.play()
    if player.rect.y >= 351:
        player.rect.y = 350
        wall.play()
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    blocks_hit_list1 = pygame.sprite.spritecollide(player, bad_block_list, True)
 
    # Check the list of collisions for good and bad blocks and update information.
    for block in blocks_hit_list:
        good_sound.play()
        score += 1
        print(score)
    
    for block in blocks_hit_list1:
        bad_sound.play()
        score -= 1
        print(score)

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Printing our score to screen by accessing the score var and converting to string to match the data type of the rest of the text
    points = font.render("MY SCORE:" + str(score),True, BLACK)
    screen.blit(points, [50, 350])
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    all_sprites_list.update()
 
    # Limit to 30 frames instead of 60 to help with performance
    clock.tick(30)
 
pygame.quit()