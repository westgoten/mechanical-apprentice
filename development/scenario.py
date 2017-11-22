import os
import pygame
from constants import BLACK, WHITE

class Template():

    def __init__(self, background, default_s):
        self.default_s = default_s
        self.next_s = default_s

        self.obtainables = pygame.sprite.Group()
        self.not_obtainables = pygame.sprite.Group()
        self.details = pygame.sprite.Group()
        self.visible_objects = pygame.sprite.Group()

        self.background = background
        self.black_screen = None

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.visible_objects.draw(screen)
        if self.black_screen != None:
            self.black_screen.draw(screen)

# -- Black Screen --
class BlackUnit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.Surface([30, 30]).convert_alpha()
        self.image.fill(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.mask = pygame.mask.from_surface(self.image)

# -- Light --
class LightRay(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load(os.path.join('data', 'images', 'scenario', 'flashlight200_30.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_threshold(self.image, WHITE, WHITE)
        
        self.black_units_removed = pygame.sprite.Group()
        
    def update(self, scenario, mouse_pos):
        self.rect.center = mouse_pos
        
        for unit in self.black_units_removed:
            if pygame.sprite.collide_mask(self, unit) == None:
                self.black_units_removed.remove(unit)
                scenario.black_screen.add(unit)
        
        black_units_collided = pygame.sprite.spritecollide(self, scenario.black_screen, True, pygame.sprite.collide_mask)
        self.black_units_removed.add(black_units_collided)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
