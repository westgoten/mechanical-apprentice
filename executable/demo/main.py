"""
Main program. Runs the entire game.
"""

import pygame
from constants import *
from game_class import Game

def main():

    pygame.init()

    # -- Set up game window --
    screen = pygame.display.set_mode([SCR_WIDTH, SCR_HEIGHT])
    pygame.display.set_caption("Aprendiz De Mecânico (demo)")

    # -- Used to set the frame rate --
    clock = pygame.time.Clock()

    # -- Used to maintain/break the main loop --
    done = False

    game = Game()

    # -- Main loop --
    while not done:
        done = game.process_events()

        game.run_logic()

        game.draw_frame(screen)

        clock.tick(60)
        pygame.display.set_caption('Aprendiz De Mecânico (demo): {}fps'.format(clock.get_fps()))

    pygame.quit()

if __name__ == '__main__':
    main()
