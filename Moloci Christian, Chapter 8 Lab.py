'''
Coded by: Christian Moloci
Chapter 8 Lab
Tuesday Septemberb 13, 2022
http://programarcadegames.com/index.php?chapter=lab_animation&lang=en
'''

import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ROAD_COLOR = (83, 86, 85)
FALL_GRASS = (248, 145, 0)
DAY_SKY = (163, 201, 213)
NIGHT_SKY = (18, 48, 103)
CAR_COLOR = (255, 26, 26)
SUN = (255, 190, 49)
TREE_TRUNK = (108, 65, 27)
LEAVES = (225, 141, 12)
MOON = (247, 242, 224)
JEANS = (20, 103, 210)
SHIRT = (201,237,148)
SKIN = (251,207,127)
TURBINE = (92, 92, 92)

# Default sun location
sun_x = 700
sun_y = 30
moon_x = 100
moon_y = 600

# Defualt car location
car_top_x = 60
car_bottom_x = 20
window_1_x = 70
window_2_x = 170
wheel_1_x = 70
wheel_2_x = 230

# Defuault Leaves Locations
leaf_1 = 120
leaf_2 = 100
leaf_3 = 90
leaf_4 = 100
leaf_5 = 120
leaf_6 = 150
leaf_7 = 170
leaf_8 = 180
leaf_9 = 170
leaf_10 = 110
leaf_11 = 160

# Default Blade locations for wind turbines
blade_1_x_l = 600
blade_1_y_l = 200
blade_1_x_r = 655
blade_1_y_r = 250

blade_2_x_l = 700
blade_2_y_l = 200
blade_2_x_r = 655
blade_2_y_r = 250

blade_3_x_l = 655
blade_3_y_l = 250
blade_3_x_r = 655
blade_3_y_r = 300

# Default locations for left arm (the waving arm)
arm_x = 290
arm_y = 320

# Defualt locations for falling leaf
leaf_x = 180
leaf_y = 300
leaf_increase = 0

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (900, 650)
screen = pygame.display.set_mode(size)
 
# Name the program window
pygame.display.set_caption("Day/Night Cycles in Autum")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    # Logic for sun, moon, and color changes
    if sun_y <= 800:
        sun_y += 5
        moon_y -= 5
        if moon_y <= 300:
            screen.fill(NIGHT_SKY)
            FALL_GRASS = (151, 111, 23)
            LEAVES = (145, 96, 36)
        if moon_y >= 301:
            screen.fill(DAY_SKY)
            FALL_GRASS = (246, 176, 76)
            LEAVES = (225, 141, 12)
    if sun_y >= 799:
        sun_y = -200
        moon_y = 650
    
    # Logic for car movement
    elif car_top_x <= 950:
        car_top_x += 5
        car_bottom_x += 5
        window_1_x += 5
        window_2_x += 5
        wheel_1_x += 5
        wheel_2_x += 5
    elif car_top_x >= 950:
        car_top_x = -170
        car_bottom_x = -210
        window_1_x = -160
        window_2_x = -60
        wheel_1_x = -160
        wheel_2_x = 0

    # Logic for tree sway
    if leaf_1 == 120:
        leaf_1 -= 5
        leaf_2 -= 5
        leaf_3 -= 5
        leaf_4 -= 5
        leaf_5 -= 5
        leaf_6 -= 5
        leaf_7 -= 5
        leaf_8 -= 5
        leaf_9 -= 5
        leaf_10 -= 5
        leaf_11 -= 5
    if leaf_1 <= 120:
        leaf_1 += 15
        leaf_2 += 15
        leaf_3 += 15
        leaf_4 += 15
        leaf_5 += 15
        leaf_6 += 15
        leaf_7 += 15
        leaf_8 += 15
        leaf_9 += 15
        leaf_10 += 15
        leaf_11 += 15
    if leaf_1 >= 120:
        leaf_1 -= 5
        leaf_2 -= 5
        leaf_3 -= 5
        leaf_4 -= 5
        leaf_5 -= 5
        leaf_6 -= 5
        leaf_7 -= 5
        leaf_8 -= 5
        leaf_9 -= 5
        leaf_10 -= 5
        leaf_11 -= 5

    # Logic for arm movement
    if arm_y == 320:
        arm_y += 20
    elif arm_y == 340:
        arm_y -= 20

    # Logic for wind turbine movement
    if blade_1_y_l == 300:
        arm_y += 20
        blade_1_y_l -= 100
        blade_2_y_l -= 100
        blade_3_y_l += 50
        blade_3_y_r += 50
    elif blade_1_y_l == 200:
        arm_y -= 20
        blade_1_y_l += 100
        blade_2_y_l += 100
        blade_3_y_l -= 50
        blade_3_y_r -= 50

    # Logic for falling leaf
    if leaf_increase < 100:
        leaf_x += 2
        leaf_y += 1
        leaf_increase += 1
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # --- Drawing code should go here

    # Sun
    pygame.draw.ellipse(screen, SUN, [sun_x, sun_y, 150, 150])

    # Moon
    pygame.draw.ellipse(screen, MOON, [moon_x, moon_y, 150, 150])

    # Ground
    pygame.draw.rect(screen, ROAD_COLOR, [0, 500, 900, 200])
    
    pygame.draw.rect(screen, FALL_GRASS, [0, 250, 900, 250])

    #Tree
    pygame.draw.rect(screen, TREE_TRUNK, [150, 300, 40, 150])

    pygame.draw.ellipse(screen, LEAVES, [leaf_1, 260, 50, 50])
    pygame.draw.ellipse(screen, LEAVES, [leaf_2, 240, 50, 50])
    pygame.draw.ellipse(screen, LEAVES, [leaf_3, 220, 50, 50])
    pygame.draw.ellipse(screen, LEAVES, [leaf_4, 200, 50, 50])
    pygame.draw.ellipse(screen, LEAVES, [leaf_5, 180, 50, 50])
    pygame.draw.ellipse(screen, LEAVES, [leaf_6, 180, 50, 50])
    pygame.draw.ellipse(screen, LEAVES, [leaf_7, 200, 50, 50])
    pygame.draw.ellipse(screen, LEAVES, [leaf_8, 220, 50, 50])
    pygame.draw.ellipse(screen, LEAVES, [leaf_9, 240, 50, 50])
    pygame.draw.ellipse(screen, LEAVES, [leaf_10, 200, 100, 100])
    pygame.draw.ellipse(screen, LEAVES, [leaf_11, 258, 50, 50])

    # Person
    pygame.draw.line(screen, SHIRT, [320, 400], [320, 320],5)
    pygame.draw.line(screen, SKIN, [320, 350], [350, 320],5)
    pygame.draw.line(screen, SKIN, [arm_x, arm_y], [320, 350],5)
    pygame.draw.ellipse(screen, SKIN, [305, 300, 30, 30], 0)
    pygame.draw.line(screen, JEANS, [320, 400], [340, 440],5)
    pygame.draw.line(screen, JEANS, [300, 440], [320, 400],5)

    # Falling Leaf
    pygame.draw.ellipse(screen, LEAVES, [leaf_x, leaf_y, 20, 10], 0)

    # Car
    pygame.draw.rect(screen, CAR_COLOR, [car_bottom_x, 500, 300, 60], 0)
    pygame.draw.rect(screen, CAR_COLOR, [car_top_x, 400, 200, 100], 0)

    pygame.draw.rect(screen, WHITE, [window_1_x, 420, 80, 60], 0)
    pygame.draw.rect(screen, WHITE, [window_2_x, 420, 80, 60], 0)
    pygame.draw.ellipse(screen, BLACK, [wheel_1_x, 525, 50, 50], 0)
    pygame.draw.ellipse(screen, BLACK, [wheel_2_x, 525, 50, 50], 0)

    # Wind Mill
    pygame.draw.rect(screen, TURBINE, [650, 240, 10, 150])
    pygame.draw.line(screen, WHITE, [blade_1_x_l, blade_1_y_l], [blade_1_x_r, blade_1_y_r],5)
    pygame.draw.line(screen, WHITE, [blade_2_x_l, blade_2_y_l], [blade_2_x_r, blade_2_y_r],5)
    pygame.draw.line(screen, WHITE, [blade_3_x_l, blade_3_y_l], [blade_3_x_r, blade_3_y_r],5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 10 frames per second to make some things look less jittery such as tree movement
    clock.tick(10)
 
# Close the window and quit.
pygame.quit()