import pygame

class Template(pygame.sprite.Sprite):

    def __init__(self, width, height, image):
        super().__init__()

        self.colors = image
        self.image = pygame.Surface([width, height]).convert()
        self.image.fill(self.colors[0]) # Por enquanto, 'image' é uma lista de cores

        self.rect = None

        self.obtained_signal = False
        self.in_inventory = False
        self.dragged = False
        self.slot = None

        self.mouse_button_hold = False

    def update(self, inventory):
        mouse_pos = pygame.mouse.get_pos()

        # Putting something obtained in inventory
        if self.obtained_signal:
            self.rect = self.image.get_rect()
            for slot in inventory.slots:
                if slot.available:
                    self.rect.topleft = slot.rect.topleft
                    slot.available = False
                    self.slot = slot
                    break
            self.obtained_signal = False
            self.in_inventory = True

    def is_dragging(self, inventory, mouse_button_hold):
        if self.in_inventory:
            mouse_pos = pygame.mouse.get_pos()
            self.mouse_button_hold = mouse_button_hold

            if self.rect.collidepoint(mouse_pos) and self.mouse_button_hold:
                self.dragged = True
                for obj in inventory.objects:
                    if not obj.dragged:
                        obj.mouse_button_hold = False

    def drag_and_release(self, inventory, mouse_pos):
        if self.dragged and self.mouse_button_hold:
            self.rect.center = mouse_pos
        elif self.dragged and not self.mouse_button_hold:
            for slot in inventory.slots:
                if slot.rect.collidepoint(mouse_pos):
                    if slot.available:
                        self.slot.available = True
                        slot.available = False
                        self.slot = slot

            self.dragged = False
            self.rect.topleft = self.slot.rect.topleft

    def draw(self, screen):
        if self.rect != None:
            screen.blit(self.image, self.rect)

class Flashlight(Template):

    def update(self, inventory):
        super().update(inventory)

        mouse_pos = pygame.mouse.get_pos()

        if self.in_inventory:
            # Interaction with a inventory object
            if self.dragged and not self.mouse_button_hold:
                for obj in inventory.objects:
                    if obj.rect.collidepoint(mouse_pos) and isinstance(obj, Batteries):
                        self.slot.available = True
                        self.slot = obj.slot
                        obj.kill()

                        self.image.fill(self.colors[1])

            # Drag & Release
            self.drag_and_release(inventory, mouse_pos)

class Batteries(Template):

    def update(self, inventory):
        super().update(inventory)

        mouse_pos = pygame.mouse.get_pos()

        if self.in_inventory:
            # Interaction with a inventory object
            if self.dragged and not self.mouse_button_hold:
                for obj in inventory.objects:
                    if obj.rect.collidepoint(mouse_pos) and isinstance(obj, Flashlight):
                        self.slot.available = True
                        self.kill()

                        obj.image.fill(obj.colors[1])

            # Drag & Release
            self.drag_and_release(inventory, mouse_pos)
