"""
Game class. Controls all the game needs inside the main loop.
"""

import os
import pygame
import scenario
import inventory
from scenario_obtainables import Obtainable
from scenario_not_obtainables import *
from inventory_objects import *
import exits_and_details as ead
from buttons import *
from constants import *

class Game():
    """ In Progress """

    # -- Set important global variables, create sprites, etc --
    def __init__(self):
        # Inventory and its objects instances
        self.bag = inventory.Inventory()

        for i in range(7):
            slot_x = self.bag.rect.x + 6.5 + 58.5 * i
            slot_y = self.bag.rect.y + 6.5
            slot_width = slot_height = 52
            dimensions = (slot_x, slot_y, slot_width, slot_height)
            
            slot = inventory.Slot(dimensions)
            self.bag.slots.append(slot)

        flashlight_i = Flashlight()
        self.bag.objects.add(flashlight_i)

        batteries_i = Batteries()
        self.bag.objects.add(batteries_i)

        warehousekey_i = WarehouseKey()
        self.bag.objects.add(warehousekey_i)

        # Main area
        background = pygame.image.load(os.path.join('data', 'images', 'scenario', 'main_area', 'main_area.png')).convert_alpha()

        main_area = scenario.Template(background, 'MAIN_AREA')

        main_area_details = [(579, 255, 194, 163, 'WAREHOUSE_ENT', True),
                              (815, 308, 96, 184, 'DEPARTMENTS', True),
                              (114, 315, 97, 187, 'PV_ROOM', False),
                              (497, 275, 26, 26, 'WORKSHOP', False)]

        for detail in main_area_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            in_demo = detail[5]
            main_area.details.add(ead.Template(main_area, dimensions, next_s, in_demo))

        # Obtainables instances
        obt_image = pygame.image.load(os.path.join('data', 'images', 'scenario', 'main_area', 'obtainables', 'flashlight.png')).convert_alpha()
        flashlight_s = Obtainable(336, 393, obt_image, Flashlight)
        main_area.obtainables.add(flashlight_s)
        main_area.visible_objects.add(flashlight_s)

        obt_image = pygame.image.load(os.path.join('data', 'images', 'scenario', 'main_area', 'obtainables', 'batteries.png')).convert_alpha()
        batteries_s = Obtainable(362, 403, obt_image, Batteries)
        main_area.obtainables.add(batteries_s)
        main_area.visible_objects.add(batteries_s)

        # Warehouse entrance
        background = pygame.image.load(os.path.join('data', 'images', 'scenario', 'warehouse_entrance', 'warehouse_ent.png')).convert_alpha()

        warehouse_ent = scenario.Template(background, 'WAREHOUSE_ENT')

        warehouse_ent_details = [(0, 626, 233, 65, 'MAIN_AREA', True),
                                 (234, 543, 166, 82, 'MAIN_AREA', True)]

        for detail in warehouse_ent_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            in_demo = detail[5]
            warehouse_ent.details.add(ead.Template(warehouse_ent, dimensions, next_s, in_demo))

        # Not obtainables instances
        state1 = pygame.image.load(os.path.join('data', 'images', 'scenario', 'warehouse_entrance', 'not_obtainables', 'warehouse_door1.png')).convert_alpha()
        state2 = pygame.image.load(os.path.join('data', 'images', 'scenario', 'warehouse_entrance', 'not_obtainables', 'warehouse_door2.png')).convert_alpha()
        state3 = pygame.image.load(os.path.join('data', 'images', 'scenario', 'warehouse_entrance', 'not_obtainables', 'warehouse_door3.png')).convert_alpha()

        warehouse_door = LockedDoor(408, 12, [state1, state2, state3], WarehouseKey, None, True)
        warehouse_ent.not_obtainables.add(warehouse_door)
        warehouse_ent.visible_objects.add(warehouse_door)

        # Departments
        background = pygame.image.load(os.path.join('data', 'images', 'scenario', 'departments', 'deptms.png')).convert_alpha()

        departments = scenario.Template(background, 'DEPARTMENTS')

        departments_details = [(173, 180, 91, 143, 'MAIN_AREA', True)]

        for detail in departments_details:
            dimensions = detail[0:4]
            next_s = detail[4]
            in_demo = detail[5]
            departments.details.add(ead.Template(departments, dimensions, next_s, in_demo))

        # Not obtainables instances
        state1 = pygame.image.load(os.path.join('data', 'images', 'scenario', 'departments', 'not_obtns', 'MD_door1.png')).convert_alpha()
        state2 = pygame.image.load(os.path.join('data', 'images', 'scenario', 'departments', 'not_obtns', 'MD_door2.png')).convert_alpha()

        department_of_materials_door = UnlockedDoor(689, 95, [state1, state2], 'MATERIALS_DEPT', True)
        departments.not_obtainables.add(department_of_materials_door)
        departments.visible_objects.add(department_of_materials_door)

        # Materials department
        background = pygame.image.load(os.path.join('data', 'images', 'scenario', 'departments', 'materials', 'materials_dept.png')).convert_alpha()

        materials_dept = scenario.Template(background, 'MATERIALS_DEPT')

        # Not obtainables (+ hidden obtainable)
        not_obt_image = pygame.image.load(os.path.join('data', 'images', 'scenario', 'departments', 'materials', 'not_obtns', 'obstacle.png')).convert_alpha()
        obt_image = pygame.image.load(os.path.join('data', 'images', 'scenario', 'departments', 'materials', 'obtns', 'warehouse_key.png')).convert_alpha()

        obstacle = Obstacle(776, 356, not_obt_image, Obtainable, [778, 376, obt_image, WarehouseKey])
        materials_dept.not_obtainables.add(obstacle)
        materials_dept.visible_objects.add(obstacle)

        not_obt_image = pygame.image.load(os.path.join('data', 'images', 'scenario', 'departments', 'materials', 'not_obtns', 'dept_door.png')).convert_alpha()

        dept_door = OpenDoor(98, 170, not_obt_image, 'DEPARTMENTS', True)
        materials_dept.not_obtainables.add(dept_door)
        materials_dept.visible_objects.add(dept_door)
        
        # Buttons
        state1 = pygame.image.load(os.path.join('data', 'images', 'scenario', 'departments', 'materials', 'buttons', 'back_arrow1.png')).convert_alpha()
        state2 = pygame.image.load(os.path.join('data', 'images', 'scenario', 'departments', 'materials', 'buttons', 'back_arrow2.png')).convert_alpha()
        
        back_arrow = ButtonJustClick(20, 621, [state1, state2], 'DEPARTMENTS')
        materials_dept.buttons.add(back_arrow)

        # Blackout
        black_screen = pygame.sprite.Group()

        for y in range(0, SCR_HEIGHT, 30):
            for x in range(0, SCR_WIDTH, 30):
                black_unit = scenario.BlackUnit(x, y)
                black_screen.add(black_unit)
        materials_dept.black_screen = black_screen
        
        # Ray of light
        self.light_ray = scenario.LightRay()

        self.scenarios_dict = {'MAIN_AREA'      : main_area,
                               'WAREHOUSE_ENT'  : warehouse_ent,
                               'WORKSHOP'       : None,
                               'PV_ROOM'        : None,
                               'DEPARTMENTS'    : departments,
                               'MATERIALS_DEPT' : materials_dept}

        self.current_scenario = self.scenarios_dict['MAIN_AREA']

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.current_scenario.obtainables.update(self.bag, event.pos)
                self.current_scenario.details.update(event.pos)
                self.current_scenario.buttons.update(self.current_scenario, True)

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
        self.current_scenario.buttons.update(self.current_scenario, False)

        self.current_scenario = self.scenarios_dict[self.current_scenario.next_s]

        if self.current_scenario != previous_scenario:
            previous_scenario.next_s = previous_scenario.default_s

    def draw_frame(self, screen):
        self.current_scenario.draw(screen)
        if self.current_scenario.black_screen != None and self.bag.flashlight_working:
            self.light_ray.draw(screen)
        elif self.current_scenario.black_screen != None and not self.bag.flashlight_working:
            self.current_scenario.buttons.draw(screen)
        self.bag.draw(screen)
        pygame.display.flip()
