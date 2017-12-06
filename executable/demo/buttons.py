import pygame

class ButtonJustClick(pygame.sprite.Sprite):

    def __init__(self, x, y, states_list, next_s):
        super().__init__()
        
        self.next_s = next_s
        
        self.state_index = 0
        self.states_list = states_list
        self.current_state = self.states_list[self.state_index]
        
        self.image = self.current_state
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self, scenario, pressed):
        mouse_x, mouse_y = pygame.mouse.get_pos()
    
        mouse_x -= self.rect.x
        mouse_y -= self.rect.y

        try:
            has_touched = self.mask.get_at((mouse_x, mouse_y))
        except IndexError:
            has_touched = False
            
        if has_touched and self.state_index == 0:
            self.state_index += 1
            self.current_state = self.states_list[self.state_index]
            self.image = self.current_state
        elif not has_touched and self.state_index > 0:
            self.state_index -= 1
            self.current_state = self.states_list[self.state_index]
            self.image = self.current_state
            
        if has_touched and pressed:
            scenario.next_s = self.next_s
