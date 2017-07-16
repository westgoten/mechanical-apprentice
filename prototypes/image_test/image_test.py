import pygame

pygame.init()

WHITE = (255, 255, 255)
SCR_WIDTH = 1010
SCR_HEIGHT = 691

screen = pygame.display.set_mode([SCR_WIDTH, SCR_HEIGHT])
pygame.display.set_caption('Test')

#image = pygame.image.load('cenario1_1.png')

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
#    screen.blit(image, (0, 0))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
