import random
from constants import *
from numpy import interp
import pygame

random.seed(3127)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent's constructor
        super().__init__()
        # -- Attributes
        # self.surface = pygame.Surface(window_dims)
        self.type = "Bitcoin"

        # ## Set location of animal initially to center of screen
        self.x = random.randint(ui_window_width,window_width)
        self.y = random.randint(0,window_height)
        self.z = random.randint(min_z,max_z)
        self.scale = self.z/max_z
        self.original_image = pygame.image.load("images/bitcoin_small.png").convert_alpha()
        self.speed = interp( self.z ,[min_z,max_z],[1,10])
        self.pos = (self.x, self.y)
        self.angle = self.speed*360

        ## Update scaled image width and height
        self.width = int(self.original_image.get_width()*self.scale)
        self.height = int(self.original_image.get_height()*self.scale)
        ## Scale image
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
        # Rotate image
        self.image = pygame.transform.rotate(self.image, self.speed*360)

    def update(self):
        self.y += self.speed
        if self.y > window_height:
            self.y = random.randint(-200,-20)