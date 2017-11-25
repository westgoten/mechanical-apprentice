import pygame
from constants import *

class LockedDoor(pygame.sprite.Sprite): 

    def __init__(self, x, y, states_list, key_class, next_s, in_demo):
        super().__init__()

        self.in_demo = in_demo

        self.key_class = key_class
        self.next_s = next_s

        self.state_index = 0
        self.states_list = states_list
        self.current_state = self.states_list[self.state_index]

        self.image = self.current_state

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.mask = pygame.mask.from_surface(self.image)

    def click(self, scenario, inventory):
        mouse_pos = pygame.mouse.get_pos()

        click_x = mouse_pos[0] - self.rect.x
        click_y = mouse_pos[1] - self.rect.y

        try:
            clicked = self.mask.get_at((click_x, click_y))
        except IndexError:
            clicked = False

        if clicked:
            if self.state_index == 0:
                print('A porta está trancada.')
            elif self.state_index == 1:
                self.state_index += 1
                self.current_state = self.states_list[self.state_index]
                self.image = self.current_state
                self.rect.y = 7
            elif self.state_index == 2:
                print('Próximo cenário!')

    def item_interaction(self, inventory):
        if self.in_demo:
            for obj in inventory.objects:
                if obj.in_inventory:
                    if self.rect.collidepoint(obj.rect.center) and isinstance(obj, self.key_class):
                        self.state_index += 1
                        self.current_state = self.states_list[self.state_index]
                        self.image = self.current_state

                        obj.kill() # Eu deveria colocar in_inventory = False?

class UnlockedDoor(pygame.sprite.Sprite):

    def __init__(self, x, y, states_list, next_s, in_demo):
        super().__init__()

        self.in_demo = in_demo

        self.next_s = next_s

        self.state_index = 0
        self.states_list = states_list
        self.current_state = self.states_list[self.state_index]

        self.image = self.current_state

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.mask = pygame.mask.from_surface(self.image)

    def click(self, scenario, inventory):
        mouse_pos = pygame.mouse.get_pos()

        click_x = mouse_pos[0] - self.rect.x
        click_y = mouse_pos[1] - self.rect.y

        try:
            clicked = self.mask.get_at((click_x, click_y))
        except IndexError:
            clicked = False

        if clicked:
            if self.in_demo:
                if self.state_index == 0:
                    self.state_index += 1
                    self.current_state = self.states_list[self.state_index]
                    self.image = self.current_state
                elif self.next_s != None:
                    scenario.next_s = self.next_s
                else:
                    print('Próximo cenário!')
            else:
                print('Área inacessível nesta versão do jogo.')

    def item_interaction(self, inventory):
        pass

class OpenDoor(pygame.sprite.Sprite):

    def __init__(self, x, y, image, next_s, in_demo):
        super().__init__()

        self.in_demo = in_demo

        self.next_s = next_s

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.mask = pygame.mask.from_surface(self.image)

    def click(self, scenario, inventory):
        mouse_pos = pygame.mouse.get_pos()

        click_x = mouse_pos[0] - self.rect.x
        click_y = mouse_pos[1] - self.rect.y

        try:
            clicked = self.mask.get_at((click_x, click_y))
        except IndexError:
            clicked = False

        if clicked:
            if self.in_demo:
                if self.next_s != None:
                    scenario.next_s = self.next_s
                else:
                    print('Próximo cenário!')
            else:
                print('Área inacessível nesta versão do jogo.')

    def item_interaction(self, inventory):
        pass

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, x, y, image, obtainable_class, obtainable_args):
        super().__init__()

        self.obtainable_class = obtainable_class
        self.obtainable_args = obtainable_args

        self.state = 'IDLE'

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.mask = pygame.mask.from_surface(self.image)

    def click(self, scenario, inventory):
        mouse_pos = pygame.mouse.get_pos()

        click_x = mouse_pos[0] - self.rect.x
        click_y = mouse_pos[1] - self.rect.y

        try:
            clicked = self.mask.get_at((click_x, click_y))
        except IndexError:
            clicked = False

        if inventory.flashlight_working:
            if clicked:
                # Lembre-se do efeito sonoro
                if self.state == 'IDLE':
                    self.rect.x += 19
                    self.state = 'MOVED'

                    warehousekey_s = self.obtainable_class(*self.obtainable_args)
                    scenario.obtainables.add(warehousekey_s)
                    scenario.visible_objects.add(warehousekey_s)

    def item_interaction(self, inventory):
        pass
