import pygame

class Obtainable(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, image, matching_class):
        super().__init__()

        self.image = pygame.Surface([width, height]).convert()
        self.image.fill(image) # Por enquanto, 'image' é uma cor

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.matching_class = matching_class

    def update(self, inventory, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            for obj in inventory.objects:
                if isinstance(obj, self.matching_class):
                    obj.obtained_signal = True
                    self.kill()
