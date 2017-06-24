import pygame

class Template(pygame.sprite.Sprite):

    def __init__(self, room, dimensions, next_r):
        super().__init__()

        self.room = room
        self.next_r = next_r
        self.rect = pygame.Rect(*dimensions)

    def update(self, mouse_click):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if mouse_click:
                self.room.next_r = self.next_r
