"""
Game class. Controls all the game needs inside the main loop.
"""

import pygame
import room
import exits_and_details as ead
from constants import *

class Game():
    """ In Progress """

    # -- Set important global variables, create sprites, etc --
    def __init__(self):
        # NÃO FAÇA O LOOP
        white_room = room.Template('WHITE_ROOM')
        white_room.background = WHITE

        white_room_details = [(0, (SCR_HEIGHT - 300) / 2, 100, 300, 'RED_ROOM'),
                              (SCR_WIDTH - 100, (SCR_HEIGHT - 300) / 2, 100, 300, 'BLUE_ROOM'),
                              ((SCR_WIDTH - 300) / 2, 0, 300, 150, 'GREEN_ROOM')]

        for detail in white_room_details:
            dimensions = detail[0:4]
            next_r = detail[4]
            white_room.details.add(ead.Template(white_room, dimensions, next_r))

        red_room = room.Template('RED_ROOM')
        red_room.background = RED

        red_room_details = [(SCR_WIDTH - 100, (SCR_HEIGHT - 300) / 2, 100, 300, 'WHITE_ROOM')]

        for detail in red_room_details:
            dimensions = detail[0:4]
            next_r = detail[4]
            red_room.details.add(ead.Template(red_room, dimensions, next_r))

        blue_room = room.Template('BLUE_ROOM')
        blue_room.background = BLUE

        blue_room_details = [(0, (SCR_HEIGHT - 300) / 2, 100, 300, 'WHITE_ROOM')]

        for detail in blue_room_details:
            dimensions = detail[0:4]
            next_r = detail[4]
            blue_room.details.add(ead.Template(blue_room, dimensions, next_r))

        green_room = room.Template('GREEN_ROOM')
        green_room.background = GREEN

        green_room_details = [((SCR_WIDTH - 300) / 2, SCR_HEIGHT - 150, 300, 150, 'WHITE_ROOM')]

        for detail in green_room_details:
            dimensions = detail[0:4]
            next_r = detail[4]
            green_room.details.add(ead.Template(green_room, dimensions, next_r))

        self.rooms_dict = {'WHITE_ROOM' : white_room,
                           'RED_ROOM'   : red_room,
                           'GREEN_ROOM' : green_room,
                           'BLUE_ROOM'  : blue_room}

        self.current_room = self.rooms_dict['WHITE_ROOM']

        self.mouse_click = False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_click = True

        return False

    def run_logic(self):
        previous_room = self.current_room
        self.current_room.update(self.mouse_click)
        if self.mouse_click == True:
            self.mouse_click = False
        # Crie outra variável para os objetos de arrastar

        self.current_room = self.rooms_dict[self.current_room.next_r]

        if self.current_room != previous_room:
            previous_room.next_r = previous_room.default_r

    def draw_frame(self, screen):
        self.current_room.draw(screen)
        pygame.display.flip()
