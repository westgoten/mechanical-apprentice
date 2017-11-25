import os
import pygame
from cursor import cursor_from_image

class Obtainable(pygame.sprite.Sprite):

    def __init__(self, x, y, image, matching_class):
        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.mask = pygame.mask.from_surface(self.image)

        self.matching_class = matching_class

        self.has_left = 0
        cursor_image = pygame.image.load(os.path.join('data', 'images', 'cursors', 'hand.png'))
        self.cursor_data = cursor_from_image(cursor_image, 16, (5, 1), (0, 0))

    def update(self, inventory, pressed):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        mouse_x -= self.rect.x
        mouse_y -= self.rect.y

        try:
            has_touched = self.mask.get_at((mouse_x, mouse_y))
        except IndexError:
            has_touched = False

        if has_touched:
            self.has_left = 1
            pygame.mouse.set_cursor(*self.cursor_data)
        elif self.has_left == 1:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            self.has_left = 0
            
        if has_touched and pressed:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            for obj in inventory.objects:
                if isinstance(obj, self.matching_class):
                    obj.obtained_signal = True
                    self.kill()
