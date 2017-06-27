"""
Game class. Controls all the game needs inside the main loop.
"""

import pygame
import scenario
import inventory
from scenario_obtainables import Obtainable
from inventory_objects import *
import exits_and_details as ead
from constants import *

class Game():
    """ In Progress """

    # -- Set important global variables, create sprites, etc --
    def __init__(self):
        # NÃO FAÇA O LOOP
        white_room = scenario.Template(WHITE, 'WHITE_ROOM')

        white_room_details = [(0, (SCR_HEIGHT - 300) // 2, 100, 300, 'RED_ROOM'),
                              (SCR_WIDTH - 100, (SCR_HEIGHT - 300) // 2, 100, 300, 'BLUE_ROOM'),
                              ((SCR_WIDTH - 300) // 2, 0, 300, 150, 'GREEN_ROOM')]

        for detail in white_room_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            white_room.details.add(ead.Template(white_room, dimensions, next_s))

        # Obtainables instances
        flashlight_s = Obtainable(200, 300, 150, 150, GRAY, white_room, Flashlight)
        white_room.obtainables.add(flashlight_s)
        white_room.visible_objects.add(flashlight_s)

        batteries_s = Obtainable(375, 275, 50, 50, YELLOW, white_room, Batteries)
        white_room.obtainables.add(batteries_s)
        white_room.visible_objects.add(batteries_s)

        # Inventory and its objects instances
        self.bag = inventory.Inventory()

        for i in range(7):
            slot_x = 10 + 90 * i
            slot_y = self.bag.rect.y + 10
            slot_width = slot_height = 80
            dimensions = (slot_x, slot_y, slot_width, slot_height)
            
            slot = inventory.Slot(dimensions)
            self.bag.slots.append(slot)

        colors = [GRAY, GREEN]
        flashlight_i = Flashlight(80, 80, colors)
        self.bag.objects.add(flashlight_i)

        colors = [YELLOW]
        batteries_i = Batteries(80, 80, colors)
        self.bag.objects.add(batteries_i)

        red_room = scenario.Template(RED, 'RED_ROOM')

        red_room_details = [(SCR_WIDTH - 100, (SCR_HEIGHT - 300) // 2, 100, 300, 'WHITE_ROOM')]

        for detail in red_room_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            red_room.details.add(ead.Template(red_room, dimensions, next_s))

        blue_room = scenario.Template(BLUE, 'BLUE_ROOM')

        blue_room_details = [(0, (SCR_HEIGHT - 300) // 2, 100, 300, 'WHITE_ROOM')]

        for detail in blue_room_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            blue_room.details.add(ead.Template(blue_room, dimensions, next_s))

        green_room = scenario.Template(GREEN, 'GREEN_ROOM')

        green_room_details = [((SCR_WIDTH - 300) // 2, SCR_HEIGHT - 150, 300, 150, 'WHITE_ROOM')]

        for detail in green_room_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            green_room.details.add(ead.Template(green_room, dimensions, next_s))

        self.scenarios_dict = {'WHITE_ROOM' : white_room,
                               'RED_ROOM'   : red_room,
                               'GREEN_ROOM' : green_room,
                               'BLUE_ROOM'  : blue_room}

        self.current_scenario = self.scenarios_dict['WHITE_ROOM']

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.current_scenario.obtainables.update(self.bag, event.pos)
                self.current_scenario.details.update(event.pos)
                for obj in self.bag.objects:
                    obj.is_dragging(self.bag, True)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for obj in self.bag.objects:
                    obj.is_dragging(self.bag, False)

        return False

    def run_logic(self):
        previous_scenario = self.current_scenario

        self.bag.update()

        self.current_scenario = self.scenarios_dict[self.current_scenario.next_s]

        if self.current_scenario != previous_scenario:
            previous_scenario.next_s = previous_scenario.default_s

    def draw_frame(self, screen):
        self.current_scenario.draw(screen)
        self.bag.draw(screen)
        pygame.display.flip()
