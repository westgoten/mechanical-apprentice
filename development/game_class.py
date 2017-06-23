"""
Game class. Controls all the game needs inside the main loop.
"""

import pygame
from constants import *

class Game():
    """ In Progress """

    # -- Set important global variables, create sprites, etc --
    def __init__(self):
        return None

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        return False

    def run_logic(self):
        return None

    def draw_frame(self, screen):
        screen.fill(WHITE)

        pygame.display.flip()
