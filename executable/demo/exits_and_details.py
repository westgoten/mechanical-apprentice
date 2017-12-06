import pygame

class Template(pygame.sprite.Sprite):

    def __init__(self, scenario, dimensions, next_s, in_demo):
        super().__init__()

        self.in_demo = in_demo

        self.scenario = scenario
        self.next_s = next_s
        self.rect = pygame.Rect(*dimensions)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.in_demo:
                self.scenario.next_s = self.next_s
            else:
                #print('Área inacessível nesta versão do jogo.')
                pass
