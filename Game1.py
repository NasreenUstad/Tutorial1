# Simple pygame program

# import and initialize the pygame library
import pygame
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode([500, 500])

# run until user asks to quit
runnig = True
while runnig:

    # did the use click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

    # fill the background with white
    screen.fill((255, 255, 255))

    # draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # flip the display
    pygame.display.flip()

# done! time to quit
pygame.quit()