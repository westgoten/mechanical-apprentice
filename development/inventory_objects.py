import os
import pygame
from constants import *

class Template(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.rect = None

        self.obtained_signal = False
        self.in_inventory = False
        self.dragged = False
        self.slot = None

        self.mouse_button_hold = False

    def update(self, inventory):
        mouse_pos = pygame.mouse.get_pos()

        # Putting something obtained in inventory
        if self.obtained_signal:
            self.rect = self.image.get_rect()
            for slot in inventory.slots:
                if slot.available:
                    self.rect.center = slot.rect.center
                    slot.available = False
                    self.slot = slot
                    break
            self.obtained_signal = False
            self.in_inventory = True

    def is_dragging(self, inventory, mouse_button_hold):
        if self.in_inventory:
            mouse_pos = pygame.mouse.get_pos()
            self.mouse_button_hold = mouse_button_hold

            if self.rect.collidepoint(mouse_pos) and self.mouse_button_hold:
                self.dragged = True
                for obj in inventory.objects:
                    if not obj.dragged:
                        obj.mouse_button_hold = False

    def drag_and_release(self, inventory, mouse_pos):
        if self.dragged and self.mouse_button_hold:
            self.rect.center = mouse_pos
        elif self.dragged and not self.mouse_button_hold:
            for slot in inventory.slots:
                if slot.rect.collidepoint(mouse_pos):
                    if slot.available:
                        self.slot.available = True
                        slot.available = False
                        self.slot = slot
                        break

            self.dragged = False
            self.rect.center = self.slot.rect.center

    def draw(self, screen):
        if self.rect != None:
            screen.blit(self.image, self.rect)

class Flashlight(Template):

    def __init__(self):
        super().__init__()

        state1 = pygame.image.load(os.path.join('data', 'images', 'inventory', 'objects', 'flashlight_1.png')).convert_alpha()
        state2 = pygame.image.load(os.path.join('data', 'images', 'inventory', 'objects', 'flashlight_2.png')).convert_alpha()
        state3 = pygame.image.load(os.path.join('data', 'images', 'inventory', 'objects', 'flashlight_3.png')).convert_alpha()

        self.state_index = 0
        self.states_list = [state1, state2, state3]
        self.current_state = self.states_list[self.state_index]

        self.image = self.current_state

        self.on = False

    def update(self, inventory, scenario, light_ray):
        super().update(inventory)

        mouse_pos = pygame.mouse.get_pos()

        if self.in_inventory:
            # Interaction with a inventory object
            if self.dragged and not self.mouse_button_hold:
                for obj in inventory.objects:
                    if obj.rect != None:
                        if obj.rect.collidepoint(mouse_pos) and isinstance(obj, Batteries):
                            self.slot.available = True
                            self.slot = obj.slot
                            obj.kill() # Eu deveria colocar in_inventory = False?

                            if self.state_index < len(self.states_list):
                                self.state_index += 1

                            self.current_state = self.states_list[self.state_index]
                            self.image = self.current_state
                            inventory.flashlight_working = True
                            break

            # Drag & Release
            self.drag_and_release(inventory, mouse_pos)

            # Turn flashlight on or off
            self.turn_on_off(scenario, light_ray, mouse_pos)

    def turn_on_off(self, scenario, light_ray, mouse_pos):
        if scenario.black_screen != None and self.state_index == 1:
            self.state_index += 1
            self.current_state = self.states_list[self.state_index]
            self.image = self.current_state
            self.on = True
        elif scenario.black_screen == None and self.state_index == 2:
            self.state_index -= 1
            self.current_state = self.states_list[self.state_index]
            self.image = self.current_state
            self.on = False

        if self.on:
            light_ray.update(scenario, mouse_pos)

class Batteries(Template):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(os.path.join('data', 'images', 'inventory', 'objects', 'batteries_i.png')).convert_alpha()

    def update(self, inventory, scenario, light_ray):
        super().update(inventory)

        mouse_pos = pygame.mouse.get_pos()

        if self.in_inventory:
            # Interaction with a inventory object
            if self.dragged and not self.mouse_button_hold:
                for obj in inventory.objects:
                    if obj.rect != None:
                        if obj.rect.collidepoint(mouse_pos) and isinstance(obj, Flashlight):
                            self.slot.available = True
                            self.kill() # Eu deveria colocar in_inventory = False?

                            if obj.state_index < len(obj.states_list):
                                obj.state_index += 1

                            obj.current_state = obj.states_list[obj.state_index]
                            obj.image = obj.current_state
                            inventory.flashlight_working = True
                            break

            # Drag & Release
            self.drag_and_release(inventory, mouse_pos)

class WarehouseKey(Template):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(os.path.join('data', 'images', 'inventory', 'objects', 'warehouse_key_i.png')).convert_alpha()

    def update(self, inventory, scenario, light_ray):
        super().update(inventory)

        mouse_pos = pygame.mouse.get_pos()

        if self.in_inventory:
            self.drag_and_release(inventory, mouse_pos)
