import pygame

scr_size = 1010, 691
screen = pygame.display.set_mode(scr_size)
pygame.display.set_caption('Screen Size Test')

picture = pygame.image.load('cenario1_1.png')
picture = pygame.transform.scale(picture, (1010, 691))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(picture, (0, 0))

    pygame.display.flip()

pygame.quit()
