'''
Programmed by: Christian Moloci

Chpater 12 Lab: Classes and Graphics

http://programarcadegames.com/index.php?chapter=lab_classes_and_graphics&lang=en

Continue from #12
'''
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#vars
loop_counter = 0
cl = 0

class Rectangle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.h = 0
        self.w = 0
        self.change_x = 0
        self.change_y = 0
        self.COLOR = (0, 0, 0)
    def draw(self):
        pygame.draw.rect(screen, self.COLOR, [self.x, self.y, self.w, self.h])
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
    
class Ellipse(Rectangle):
    def __init__(self):
        super().__init__()
    def draw(self):
        pygame.draw.ellipse(screen, self.COLOR, [self.x, self.y, self.w, self.h])


pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create a list to store numbers to output our shapes
my_list = []

# Creats random numbers and appends the to our newly made list
for i in range(1000):
    my_object = Rectangle()
    my_object.x = random.randint(0, 700)
    my_object.y = random.randint(0, 500)
    my_object.h = random.randint(20, 70)
    my_object.w = random.randint(20, 70)
    cs1 = random.randrange(0, 255)
    cs2 = random.randrange(0, 255)
    cs3 = random.randrange(0, 255)
    my_object.change_x = random.randint(-3, 3)
    my_object.change_y = random.randint(-3, 3)

    my_list.append(my_object.x)
    my_list.append(my_object.y)
    my_list.append(my_object.h)
    my_list.append(my_object.w)
    my_list.append(cs1)
    my_list.append(cs2)
    my_list.append(cs3)

# create a second list for our Ellipse values
my_second_list = []

# Assings properties to newly made list for our ellipse properties
for i in range(1000):
    my_second_object = Ellipse()
    my_second_object.x = random.randint(0, 700)
    my_second_object.y = random.randint(0, 500)
    my_second_object.h = random.randint(20, 70)
    my_second_object.w = random.randint(20, 70)
    cs1 = random.randrange(0, 255)
    cs2 = random.randrange(0, 255)
    cs3 = random.randrange(0, 255)
    my_second_object.change_x = random.randint(-3, 3)
    my_second_object.change_y = random.randint(-3, 3)

    my_second_list.append(my_second_object.x)
    my_second_list.append(my_second_object.y)
    my_second_list.append(my_second_object.h)
    my_second_list.append(my_second_object.w)
    my_second_list.append(cs1)
    my_second_list.append(cs2)
    my_second_list.append(cs3)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here

    # Loop to display 1000 randomized rectangles
    while loop_counter <= 999:
        my_object.x = my_list[loop_counter]
        loop_counter += 1

        my_object.y = my_list[loop_counter]
        loop_counter += 1

        my_object.h = my_list[loop_counter]
        loop_counter += 1

        my_object.w = my_list[loop_counter]
        loop_counter += 1

        a = my_list[loop_counter]
        loop_counter += 1

        b = my_list[loop_counter]
        loop_counter += 1

        c = my_list[loop_counter]
        loop_counter += 1

        my_object.COLOR = (a, b, c)

        my_object.draw()

    # Resets the counter so we can reuse it
    loop_counter = 0

    # Loop to display 1000 randomized ellipses
    while loop_counter <= 999:
        my_second_object.x = my_second_list[loop_counter]
        loop_counter += 1

        my_second_object.y = my_second_list[loop_counter]
        loop_counter += 1

        my_second_object.h = my_second_list[loop_counter]
        loop_counter += 1

        my_second_object.w = my_second_list[loop_counter]
        loop_counter += 1

        a = my_second_list[loop_counter]
        loop_counter += 1

        b = my_second_list[loop_counter]
        loop_counter += 1

        c = my_second_list[loop_counter]
        loop_counter += 1

        my_second_object.COLOR = (a, b, c)

        my_second_object.draw()

    # Resets the counter so we can repeat the process the next time around
    loop_counter = 0
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(10)
 
# Close the window and quit.
pygame.quit()