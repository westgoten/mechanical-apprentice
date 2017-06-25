import pygame

class Template():

    def __init__(self, default_r):
        self.default_r = default_r
        self.next_r = default_r

        self.objects = pygame.sprite.Group()
        self.details = pygame.sprite.Group()

        self.background = (0, 0, 0)

    def update(self):
        self.objects.update()

    def draw(self, screen):
        screen.fill(self.background)
        self.objects.draw(screen)
