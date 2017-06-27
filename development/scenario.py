import pygame

class Template():

    def __init__(self, background, default_s):
        self.default_s = default_s
        self.next_s = default_s

        self.obtainables = pygame.sprite.Group()
        self.not_obtainables = pygame.sprite.Group()
        self.details = pygame.sprite.Group()
        self.visible_objects = pygame.sprite.Group()

        self.background = background

    def draw(self, screen):
        screen.fill(self.background) # Por enquanto, 'background' é uma cor
        self.visible_objects.draw(screen)
