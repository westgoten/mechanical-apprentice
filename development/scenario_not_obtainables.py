import pygame
from constants import *

class Door(pygame.sprite.Sprite): 

    def __init__(self, x, y, states_list, key_class, next_s):
        super().__init__()

        self.key_class = key_class
        self.next_s = next_s

        self.size = (100, 200)

        self.state_index = 0
        self.states_list = states_list
        self.current_state = self.states_list[self.state_index]

        self.image = pygame.Surface(self.size)
        self.image.fill(self.current_state)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def click(self, scenario):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if self.state_index == 0:
                print('A porta está trancada.')
            elif self.state_index == 1:
                self.state_index += 1
                self.current_state = self.states_list[self.state_index]
                self.image.fill(self.current_state)
            elif self.state_index == 2:
                print('Próximo cenário!')

    def item_interaction(self, inventory):
        for obj in inventory.objects:
            if obj.in_inventory:
                if self.rect.collidepoint(obj.rect.center) and isinstance(obj, self.key_class):
                    self.state_index += 1
                    self.current_state = self.states_list[self.state_index]
                    self.image.fill(self.current_state)

                    obj.kill()
