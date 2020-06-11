# Simple pygame program

# Before you start writing any code, it’s always a good idea to have some design in place.
# Since this is a tutorial game, let’s design some basic gameplay for it as well:
#
# The goal of the game is to avoid incoming obstacles:
# The player starts on the left side of the screen.
# The obstacles enter randomly from the right and move left in a straight line.
# The player can move left, right, up, or down to avoid the obstacles.
# The player cannot move off the screen.
# The game ends either when the player is hit by an obstacle or when the user closes the window.


# import and initialize the pygame library
import pygame

# import pygame.locals for easier access to key coordinates
# updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# initialize pygame
pygame.init()


# define a Player object by extending pygame.sprite.Sprite
# the surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # move the sprite based on user key presses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# define constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create the screen object
# the size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
# set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# instantiate player, Right now, this is just a rectangle.
player = Player()

# Setting up the game loop
        # Every game from Pong to Fortnite uses a game loop to control gameplay.
        # The game loop does four very important things:
        #
        # Processes user input
        # Updates the state of all game objects
        # Updates the display and audio output
        # Maintains the speed of the game

# variable to keep the main loop running
running = True

# Main loop
while running:

    # look at every event in the queue
    for event in pygame.event.get():
        # did the user hit a key?
        if event.type == KEYDOWN:
            # was it the ESCAPE key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # did the user click window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

    # get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # update the player sprite based on user key presses
    player.update(pressed_keys)

    # fill the background with black
    screen.fill((0, 0, 0))

    # create a surface and pass in a tuple containing its length and width
    # surf = pygame.Surface((50, 50))

    # rect = surf.get_rect()

    # put the center of the surf at the center of the display
    # surf_center = ((SCREEN_WIDTH - surf.get_width())/2,
    #                (SCREEN_HEIGHT - surf.get_height())/2)

    # this line says "draw surf onto the screen at the center
    # screen.blit(surf, surf_center)

    # draw the player on the screen
    # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(player.surf, player.rect)

    # update the display
    pygame.display.flip()

# done! time to quit
pygame.quit()

# In programming terms, a sprite is a 2D representation of something on the screen.
