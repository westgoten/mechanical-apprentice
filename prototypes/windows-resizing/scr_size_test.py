import pygame

scr_size = 1352, 691
pygame.display.set_mode(scr_size)
pygame.display.set_caption('Screen Size Test')

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
