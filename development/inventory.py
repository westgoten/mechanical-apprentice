import pygame
from constants import *

class Inventory():

    def __init__(self):
        self.image = pygame.Surface([SCR_WIDTH, 171])
        self.image.fill(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, (SCR_HEIGHT - 171))
        
        self.slots = []
        
        for i in range(7):
            slot_x = 30 + (850 // 7 + 20) * i
            slot_y = self.rect.y + 20
            slot_width = slot_height = 850 // 7
            dimensions = (slot_x, slot_y, slot_width, slot_height)
            
            slot = Slot(dimensions)
            self.slots.append(slot)
            
    def search_free_slot(self, room_object):
        for slot in self.slots:
            if slot.available:
                # Crie os objetos obtíveis primeiro
            
class Slot(pygame.sprite.Sprite):

    def __init__(self, dimensions):
        super().__init__()
        
        self.rect = pygame.Rect(*dimensions)
        
        self.available = True
    