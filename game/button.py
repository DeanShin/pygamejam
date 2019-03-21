class Button():

    def __init__(self, pygame, fontpath, fontsize, x, y, w, h, ic, hc, ac, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.font.Font(fontpath, fontsize)
        self.text_surface = self.font.render(text, True, ic, (63,63,63))
        self.ac = ac
        self.hc = hc
        self.ic = ic
        self.color = ic
        self.thickness = 2
        self.text_pos = ((x+(w/2)-self.text_surface.get_width()/2), (y+(h/2)-self.text_surface.get_height()/2))

    def handle_event(self, pygame, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.color = self.ac

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            mouse_hovering = True
        else:
            mouse_hovering = False
        self.color = self.hc if mouse_hovering else self.ic

    def draw(self, pygame, window)
        # Blit the rect.
        pygame.draw.rect(window, self.color, self.rect, self.thickness)
        # Blit the text.
        window.blit(self.text_surface, self.text_pos)
