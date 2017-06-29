import pygame
from constants import *

class LockedDoor(pygame.sprite.Sprite): 

    def __init__(self, x, y, states_list, key_class, next_s, in_demo):
        super().__init__()

        self.in_demo = in_demo

        self.key_class = key_class
        self.next_s = next_s

        self.size = (100, 200)

        self.state_index = 0
        self.states_list = states_list
        self.current_state = self.states_list[self.state_index]

        self.image = pygame.Surface(self.size).convert()
        self.image.fill(self.current_state)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def click(self, scenario, inventory):
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
        if self.in_demo:
            for obj in inventory.objects:
                if obj.in_inventory:
                    if self.rect.collidepoint(obj.rect.center) and isinstance(obj, self.key_class):
                        self.state_index += 1
                        self.current_state = self.states_list[self.state_index]
                        self.image.fill(self.current_state)

                        obj.kill()

class UnlockedDoor(pygame.sprite.Sprite):

    def __init__(self, x, y, states_list, next_s, in_demo):
        super().__init__()

        self.in_demo = in_demo

        self.next_s = next_s

        self.size = (100, 200)

        self.state_index = 0
        self.states_list = states_list
        self.current_state = self.states_list[self.state_index]

        self.image = pygame.Surface(self.size).convert()
        self.image.fill(self.current_state)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def click(self, scenario, inventory):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if self.in_demo:
                if self.state_index == 0:
                    self.state_index += 1
                    self.current_state = self.states_list[self.state_index]
                    self.image.fill(self.current_state)
                elif self.next_s != None:
                    scenario.next_s = self.next_s
                else:
                    print('Próximo cenário!')
            else:
                print('Área inacessível nesta versão do jogo.')

    def item_interaction(self, inventory):
        pass

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, x, y, states_list, obtainable_class, obtainable_args):
        super().__init__()

        self.obtainable_class = obtainable_class
        self.obtainable_args = obtainable_args

        self.size = (100, 100)

        self.state_index = 0
        self.states_list = states_list
        self.current_state = self.states_list[self.state_index]

        self.image = pygame.Surface(self.size).convert()
        self.image.fill(self.current_state)

        self.rect = self.image.get_rect()
        self.rect.x = x - 10
        self.rect.y = y - self.size[1] + 50

    def click(self, scenario, inventory):
        mouse_pos = pygame.mouse.get_pos()

        if inventory.flashlight_working:
            if self.rect.collidepoint(mouse_pos):
                # Lembre-se do efeito sonoro
                if self.state_index == 0:
                    self.rect.x += 50 + 20
                    self.state_index += 1

                    warehousekey_s = self.obtainable_class(*self.obtainable_args)
                    scenario.obtainables.add(warehousekey_s)
                    scenario.visible_objects.add(warehousekey_s)

    def item_interaction(self, inventory):
        pass
