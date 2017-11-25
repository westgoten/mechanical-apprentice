import pygame

class Obtainable(pygame.sprite.Sprite):

    def __init__(self, x, y, image, matching_class):
        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.mask = pygame.mask.from_surface(self.image)

        self.matching_class = matching_class

    def update(self, inventory, mouse_pos):
        mouse_x, mouse_y = mouse_pos

        mouse_x -= self.rect.x
        mouse_y -= self.rect.y

        try:
            clicked = self.mask.get_at((mouse_x, mouse_y))
        except IndexError:
            clicked = False
            
        if clicked:
            for obj in inventory.objects:
                if isinstance(obj, self.matching_class):
                    obj.obtained_signal = True
                    self.kill()
