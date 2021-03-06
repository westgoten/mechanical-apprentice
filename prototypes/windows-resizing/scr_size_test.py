import pygame

scr_size = 1010, 691
screen = pygame.display.set_mode(scr_size)
pygame.display.set_caption('Screen Size Test')

picture = pygame.image.load('departamentos.png')

porta_1 = pygame.image.load('porta_do_DM1.png')
porta_2 = pygame.image.load('porta_do_DM2.png')

no = 0
portas = [porta_1, porta_2]
porta_atual = portas[no]

porta_rect_1 = porta_1.get_rect()
porta_rect_1.topleft = (689, 95)

porta_rect_2 = porta_2.get_rect()
porta_rect_2.topleft = (690, 95)

portas_r = [porta_rect_1, porta_rect_2]
porta_atual_r = portas_r[no]

inventory = pygame.image.load('inventario.png')
inv_rect = inventory.get_rect()

inv_rect.x = (1010 - inv_rect.width) / 2
inv_rect.y = (691 - inv_rect.height)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                no += 1
                if no > 1:
                    no = 0

                porta_atual = portas[no]
                porta_atual_r = portas_r[no]

    screen.blit(picture, (0, 0))
    screen.blit(porta_atual, porta_atual_r)
    screen.blit(inventory, inv_rect)

    pygame.display.flip()

pygame.quit()
