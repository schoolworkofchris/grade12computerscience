"""
Coded By Chris
Template: Pygame Base Template

Chapter 10 Lab: Controlling Objects
"""

'''
How to play:
Move the square perfectly into the slot using the mouse cursor.
Move the circle perfectly into the slot by using the arrow keys on your keyboard.
'''
 
# Import needed libraries
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SQUARE_GREEN = (21, 158, 68)
ELLIPSE_BLUE = (21, 141, 158)
FONT_COLOR = (27, 27, 27)
SQUARE_YELLOW = (245, 236, 127)
SQUARE_RED = (216, 7, 7)
ELLIPSE_PURPLE = (108, 7, 216)
BACKGROUND = (27, 27, 27)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Chapter 10 Lab: Controlling Stuff")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Default starting coordinates for the circle
x_coord = 0
y_coord = 0
x_speed = 0
y_speed = 0

# Funtion to draw the controllable square
def playerSquare(mouse_x, mouse_y):
    pygame.draw.rect(screen, SQUARE_GREEN, [mouse_x, mouse_y, 150, 150])
    pygame.draw.rect(screen, SQUARE_YELLOW, [mouse_x+25, mouse_y+25, 100, 100])
    pygame.draw.ellipse(screen, SQUARE_RED, [mouse_x+25, mouse_y+25, 100, 100])

# Funtion to draw the controllable Ellipse (Circle)
def playerCircle(x_coord, y_coord):
    pygame.draw.ellipse(screen, ELLIPSE_BLUE, [x_coord, y_coord, 150, 150])
    pygame.draw.ellipse(screen, ELLIPSE_PURPLE, [x_coord+25, y_coord+25, 100, 100])

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -1
            elif event.key == pygame.K_RIGHT:
                x_speed = 1
            elif event.key == pygame.K_UP:
                y_speed = -1
            elif event.key == pygame.K_DOWN:
                y_speed = 1
    
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    # checks whether the square is on screen or not ant places it back if it is off screen
    if x_coord <= -150 :
        x_coord = 699
    if x_coord >= 700:
        x_coord = -150

    if y_coord <= -150 :
        y_coord = 499
    if y_coord >= 500:
        y_coord = -150

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed
 
    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]

    # Makes text visible saying "You Win!!" by changing the color to white when the user has perfectly aligned both shapes
    if mouse_x == 100 and mouse_y == 200 and x_coord == 450 and y_coord == 200:
        FONT_COLOR = (255, 255, 255)

    # Non visible "You Win!!" Text
    font = pygame.font.SysFont('Arial Rounded MT Bold', 100, True, False)
    win_text = font.render("You Win!!", True, FONT_COLOR)

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND)
 
    # --- Drawing code should go here

    # Displays the "Line em up!" text
    font = pygame.font.SysFont('Arial Rounded MT Bold', 100, True, False)
    title = font.render("Line em up!", True, WHITE)
    
    # Displays all the text by bliting
    screen.blit(title, [100, 100])
    screen.blit(win_text, [150, 400])

    # Draw some background colors
    pygame.draw.rect(screen, WHITE, [100, 200, 150, 150])
    pygame.draw.ellipse(screen, WHITE, [450, 200, 150, 150])

    # Calls funcitons and displays the shapes at the keyboards and mouses coordinated
    playerSquare(mouse_x, mouse_y)
    playerCircle(x_coord, y_coord)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()