import pygame
from pygame.locals import *

pygame.init()

pic=pygame.image.load("original_scroll.png") #You need an example picture in the same folder as this file!
pic_size = pic.get_size()
screen=pygame.display.set_mode((0, 0), FULLSCREEN)
scr_size = screen.get_size()
screen.blit(pygame.transform.scale(pic, scr_size), (0, 0))
pygame.display.flip()

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
#    elif event.type==VIDEORESIZE:
#        screen=pygame.display.set_mode(event.size, RESIZABLE)
#        screen.blit(pygame.transform.scale(pic, event.size), (0, 0))
#        pygame.display.flip()
#        clock.tick(30)

pygame.quit()
