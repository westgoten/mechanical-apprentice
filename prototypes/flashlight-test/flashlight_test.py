import pygame

pygame.init()

# -- Colors --
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

# -- Used to set frame rate
clock = pygame.time.Clock()

# -- Set up display --
SCR_WIDTH, SCR_HEIGHT = (1010, 691)
screen = pygame.display.set_mode([SCR_WIDTH, SCR_HEIGHT])
pygame.display.set_caption('Lantern Test. FPS: {}'.format(clock.get_fps()))

class BlackUnit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.Surface([30, 30]).convert_alpha()
        self.image.fill(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.mask = pygame.mask.from_surface(self.image)
        
class Lantern(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load('flashlight200_30.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_threshold(self.image, WHITE, WHITE)
        
        self.black_units_removed = pygame.sprite.Group()
        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        
        self.rect.center = mouse_pos
        
        for unit in self.black_units_removed:
            if pygame.sprite.collide_mask(self, unit) == None:
                self.black_units_removed.remove(unit)
                black_screen.add(unit)
        
        black_units_collided = pygame.sprite.spritecollide(self, black_screen, True, pygame.sprite.collide_mask)
        self.black_units_removed.add(black_units_collided)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
# -- Sprite Groups --
black_screen = pygame.sprite.Group()

# -- Sprites --
for y in range(0, SCR_HEIGHT, 30):
    for x in range(0, SCR_WIDTH, 30):
        black_unit = BlackUnit(x, y)
        black_screen.add(black_unit)
        
lantern = Lantern()

# -- Used to hold/break the main loop --
done = False

# -- Main loop --
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    lantern.update()
            
    screen.fill(RED)
    
    black_screen.draw(screen)
    lantern.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption('Lantern Test. FPS: {}'.format(clock.get_fps()))
    
pygame.quit()
