import pygame

class Template(pygame.sprite.Sprite):

    def __init__(self, scenario, dimensions, next_s):
        super().__init__()

        self.scenario = scenario
        self.next_s = next_s
        self.rect = pygame.Rect(*dimensions)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.scenario.next_s = self.next_s
