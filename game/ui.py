class UI():
    def __init__(self, pygame):
        self.surface = pygame.Surface((900,600))
        self.surface.set_colorkey((0,0,0))
        self.font = pygame.font.SysFont('arial.ttf', 20)
        self.bgcolor = (15,15,255)
        self.olcolor = (255,255,255)
        self.main_rects = []
        self.main_rects.append((5,5,190,390))
        self.main_rects.append((5,405,190,190))
    def handle_event(self, gens, pygame, event):
        for gen in gens:
            gen.handle_event(pygame, event)
    def hover_check(self, gens, mouse_pos):
        for gen in gens:
            gen.hover_check(mouse_pos)
        pass
    def draw(self, pygame, sur, gens):
        for main_rect in self.main_rects:
            pygame.draw.rect(self.surface, self.bgcolor, main_rect)
            pygame.draw.rect(self.surface, self.olcolor, main_rect, 10)
        for gen in gens:
            gen.draw(pygame, self.surface)
        sur.blit(self.surface, (0,0))
        