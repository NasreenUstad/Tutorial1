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
import random

# import pygame.locals for easier access to key coordinates
# updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
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
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 160, 255))

        # if you have image the uncomment below code
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

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


# define the enemy object by extending pygame.sprite.Sprite
# the surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 255, 255))
        # surf_center = ((SCREEN_WIDTH - self.surf.get_width())/2, (SCREEN_HEIGHT - self.surf.get_height())/2)
        # print(surf_center)
        # self.rect = self.surf.get_rect(center=surf_center)

        # if you have image the uncomment below code
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        # the starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100),
                random.randint(0, SCREEN_HEIGHT))
        )
        self.speed = random.randint(5, 10)
        # print(self.speed)

    # move the sprite based on speed
    # remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("clouds.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# define constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create the screen object
# the size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
# set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# create a custom event for adding a new enemy
ADD_ENEMY = pygame.USEREVENT + 1
# print(ADD_ENEMY)
pygame.time.set_timer(ADD_ENEMY, 250)
ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 1000)

# total 3 lifelines
lifeline = 3


# instantiate player, Right now, this is just a rectangle.
player = Player()

# create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


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

        # add a new enemy
        elif event.type == ADD_ENEMY:
            # create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new cloud?
        elif event.type == ADD_CLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # update the player sprite based on user key presses
    player.update(pressed_keys)

    # update enemy position and clouds
    enemies.update()
    clouds.update()

    # Fill the screen with sky blue
    screen.fill((135, 206, 250))

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
    # screen.blit(player.surf, player.rect)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # print(lifeline)
        # if so, then remove the player and stop the loop
        player.kill()
        # running = False

        if lifeline > 1:
            # restart the game by removing enemies from all_sprites and empty the enemies
            all_sprites.remove(enemies)
            enemies.empty()
            player = Player()
            all_sprites.add(player)
            # decrease the lifeline by 1 till it reaches to 0
            lifeline -= 1
        else:
            running = False

    # update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# done! time to quit
pygame.quit()

# In programming terms, a sprite is a 2D representation of something on the screen.
