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
        click_x = mouse_pos[0] - self.rect.x
        click_y = mouse_pos[1] - self.rect.y

        try:
            clicked = self.mask.get_at((click_x, click_y))
        except IndexError:
            clicked = False

        if clicked:
            for obj in inventory.objects:
                if isinstance(obj, self.matching_class):
                    obj.obtained_signal = True
                    self.kill()
