import os
import pygame
from constants import *
from find_data import find_data_file

class Inventory():

    def __init__(self):
        self.image = pygame.image.load(find_data_file(os.path.join('data', 'images', 'inventory', 'inventory.png'))).convert()
        
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCR_WIDTH - self.rect.width) / 2, (SCR_HEIGHT - self.rect.height))
        
        self.slots = []
        self.objects = pygame.sprite.Group()

        self.flashlight_working = False

    def update(self, scenario, light_ray):
        self.objects.update(self, scenario, light_ray)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        last_to_blit = None

        for obj in self.objects:
            if not obj.dragged:
                obj.draw(screen)
            else:
                last_to_blit = obj

        if last_to_blit != None:
            last_to_blit.draw(screen)

class Slot(pygame.sprite.Sprite):

    def __init__(self, dimensions):
        super().__init__()
        
        self.rect = pygame.Rect(*dimensions)
        
        self.available = True
    