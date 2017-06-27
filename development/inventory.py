import pygame
from constants import *

class Inventory():

    def __init__(self):
        self.image = pygame.Surface([(7*80 + 6*10 + 2*10), 100]).convert()
        self.image.fill(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, (SCR_HEIGHT - 100))
        
        self.slots = []
        self.objects = pygame.sprite.Group()

    def update(self):
        self.objects.update(self)

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
    