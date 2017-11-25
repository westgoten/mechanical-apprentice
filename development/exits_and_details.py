import os
import pygame
from cursor import cursor_from_image

class Template(pygame.sprite.Sprite):

    def __init__(self, scenario, dimensions, next_s, in_demo):
        super().__init__()

        self.in_demo = in_demo

        self.scenario = scenario
        self.next_s = next_s
        self.rect = pygame.Rect(*dimensions)

        self.has_left = 0
        cursor_image = pygame.image.load(os.path.join('data', 'images', 'cursors', 'hand.png'))
        self.cursor_data = cursor_from_image(cursor_image, 16, (5, 1), (0, 0))

    def update(self, pressed):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.has_left = 1
            pygame.mouse.set_cursor(*self.cursor_data)
        elif self.has_left == 1:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            self.has_left = 0

        if self.rect.collidepoint(mouse_pos) and pressed:
            if self.in_demo:
                self.scenario.next_s = self.next_s
            else:
                print('Área inacessível nesta versão do jogo.')
