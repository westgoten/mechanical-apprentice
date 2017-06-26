import pygame

class Template(pygame.sprite.Sprite):

    def __init__(self, width, height, image, scenario):
        super().__init__()

        self.image = pygame.Surface([width, height]).convert()
        self.image.fill(image) # Por enquanto, 'image' é uma cor

        self.rect = None

        self.obtained_signal = False
        self.in_inventory = False

    def update(self, inventory):
        if self.obtained_signal:
            self.rect = self.image.get_rect()
            for slot in inventory.slots:
                if slot.available:
                    self.rect.topleft = slot.rect.topleft
                    slot.available = False
                    break
            self.obtained_signal = False
            self.in_inventory = True

    def draw(self, screen):
        if self.rect != None:
            screen.blit(self.image, self.rect)

class Flashlight(Template):

    def update(self, inventory):
        super().update(inventory)
