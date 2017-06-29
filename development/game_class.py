"""
Game class. Controls all the game needs inside the main loop.
"""

import pygame
import scenario
import inventory
from scenario_obtainables import Obtainable
from scenario_not_obtainables import *
from inventory_objects import *
import exits_and_details as ead
from constants import *

class Game():
    """ In Progress """

    # -- Set important global variables, create sprites, etc --
    def __init__(self):
        # Inventory and its objects instances
        self.bag = inventory.Inventory()

        for i in range(7):
            slot_x = 10 + 90 * i
            slot_y = self.bag.rect.y + 10
            slot_width = slot_height = 80
            dimensions = (slot_x, slot_y, slot_width, slot_height)
            
            slot = inventory.Slot(dimensions)
            self.bag.slots.append(slot)

        flashlight_i = Flashlight()
        self.bag.objects.add(flashlight_i)

        batteries_i = Batteries()
        self.bag.objects.add(batteries_i)

        warehousekey_i = WarehouseKey()
        self.bag.objects.add(warehousekey_i)

        # White room
        white_room = scenario.Template(WHITE, 'WHITE_ROOM')

        white_room_details = [(0, (SCR_HEIGHT - 300) // 2, 100, 300, 'RED_ROOM', True),
                              (SCR_WIDTH - 100, (SCR_HEIGHT - 300) // 2, 100, 300, 'BLUE_ROOM', True),
                              ((SCR_WIDTH - 300) // 2, 0, 300, 150, 'GREEN_ROOM', True)]

        for detail in white_room_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            in_demo = detail[5]
            white_room.details.add(ead.Template(white_room, dimensions, next_s, in_demo))

        # Obtainables instances
        flashlight_s = Obtainable(200, 300, 150, 150, GRAY, Flashlight)
        white_room.obtainables.add(flashlight_s)
        white_room.visible_objects.add(flashlight_s)

        batteries_s = Obtainable(375, 275, 50, 50, YELLOW, Batteries)
        white_room.obtainables.add(batteries_s)
        white_room.visible_objects.add(batteries_s)

        # Red room
        red_room = scenario.Template(RED, 'RED_ROOM')

        red_room_details = [(SCR_WIDTH - 100, (SCR_HEIGHT - 300) // 2, 100, 300, 'WHITE_ROOM', True)]

        for detail in red_room_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            in_demo = detail[5]
            red_room.details.add(ead.Template(red_room, dimensions, next_s, in_demo))

        # Not obtainables instances
        warehouse_door = LockedDoor(SCR_WIDTH - 200, 200, [BROWN, SOFT_GREEN, WHITE], WarehouseKey, None, True)
        red_room.not_obtainables.add(warehouse_door)
        red_room.visible_objects.add(warehouse_door)

        # Blue room
        blue_room = scenario.Template(BLUE, 'BLUE_ROOM')

        blue_room_details = [(0, (SCR_HEIGHT - 300) // 2, 100, 300, 'WHITE_ROOM', True)]

        for detail in blue_room_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            in_demo = detail[5]
            blue_room.details.add(ead.Template(blue_room, dimensions, next_s, in_demo))

        # Not obtainables instances
        department_of_materials_door = UnlockedDoor(SCR_WIDTH - 200, 200, [SOFT_GREEN, WHITE], 'SYELLOW_ROOM', True)
        blue_room.not_obtainables.add(department_of_materials_door)
        blue_room.visible_objects.add(department_of_materials_door)

        # Green room
        green_room = scenario.Template(GREEN, 'GREEN_ROOM')

        green_room_details = [((SCR_WIDTH - 300) // 2, SCR_HEIGHT - 150, 300, 150, 'WHITE_ROOM', True)]

        for detail in green_room_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            in_demo = detail[5]
            green_room.details.add(ead.Template(green_room, dimensions, next_s, in_demo))

        # Soft yellow room
        syellow_room = scenario.Template(SOFT_YELLOW, 'SYELLOW_ROOM')

        syellow_room_details = [((SCR_WIDTH - 300) // 2, SCR_HEIGHT - 150, 300, 150, 'BLUE_ROOM', True)]

        for detail in syellow_room_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            in_demo = detail[5]
            syellow_room.details.add(ead.Template(syellow_room, dimensions, next_s, in_demo))

        # Not obtainables
        obstacle = Obstacle(200, 200, [GRAY], Obtainable, [200, 200, 50, 50, SOFT_BLUE, WarehouseKey])
        syellow_room.not_obtainables.add(obstacle)
        syellow_room.visible_objects.add(obstacle)

        # Blackout
        black_screen = pygame.sprite.Group()

        for y in range(0, SCR_HEIGHT, 30):
            for x in range(0, SCR_WIDTH, 30):
                black_unit = scenario.BlackUnit(x, y)
                black_screen.add(black_unit)
        syellow_room.black_screen = black_screen
        
        # Ray of light
        self.light_ray = scenario.LightRay()

        self.scenarios_dict = {'WHITE_ROOM'   : white_room,
                               'RED_ROOM'     : red_room,
                               'GREEN_ROOM'   : green_room,
                               'BLUE_ROOM'    : blue_room,
                               'SYELLOW_ROOM' : syellow_room}

        self.current_scenario = self.scenarios_dict['WHITE_ROOM']

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.current_scenario.obtainables.update(self.bag, event.pos)
                self.current_scenario.details.update(event.pos)

                for obj in self.current_scenario.not_obtainables:
                    obj.click(self.current_scenario, self.bag)

                for obj in self.bag.objects:
                    obj.is_dragging(self.bag, True)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for obj in self.bag.objects:
                    obj.is_dragging(self.bag, False)

                for obj in self.current_scenario.not_obtainables:
                    obj.item_interaction(self.bag)

        return False

    def run_logic(self):
        previous_scenario = self.current_scenario

        self.bag.update(self.current_scenario, self.light_ray)

        self.current_scenario = self.scenarios_dict[self.current_scenario.next_s]

        if self.current_scenario != previous_scenario:
            previous_scenario.next_s = previous_scenario.default_s

    def draw_frame(self, screen):
        self.current_scenario.draw(screen)
        if self.current_scenario.black_screen != None and self.bag.flashlight_working:
            self.light_ray.draw(screen)
        self.bag.draw(screen)
        pygame.display.flip()
