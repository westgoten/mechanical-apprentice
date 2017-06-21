import pygame
import time
from pygame.locals import *

pygame.init()

pic=pygame.image.load("resized_scroll_by_gimp.png") #You need an example picture in the same folder as this file!
pic2=pygame.image.load("resized_scroll_by_ink.png")

pic_size = pic.get_size()
pic2_size = pic2.get_size()

i = 0
pics = [pic, pic2]

screen=pygame.display.set_mode((0, 0), FULLSCREEN)
scr_size = screen.get_size()
screen.blit(pics[i], (0, 0))
#screen.blit(pygame.transform.scale(pic, scr_size), (0, 0))
pygame.display.flip()
ti = time.time()

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    tf = time.time()
    t = tf - ti

    if t > 5:
        i += 1
        if i > 1:
            i = 0
        screen.blit(pics[i], (0, 0))
        pygame.display.flip()
        ti = time.time()

#    elif event.type==VIDEORESIZE:
#        screen=pygame.display.set_mode(event.size, RESIZABLE)
#        screen.blit(pygame.transform.scale(pic, event.size), (0, 0))
#        pygame.display.flip()
#        clock.tick(30)

pygame.quit()
