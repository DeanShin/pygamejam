from money_generator import MoneyGenerator as MG
from button import Button as BN

class UI():
    def __init__(self, pygame):
        self.surface = pygame.Surface((900,600))
        self.bgcolor = (15,15,255)
        self.olcolor = (255,255,255)
        self.s1_rect = (5,5,190,390)
        self.s2_rect = (5,405,190,190)
        self.gens = []
        pass
    def update(self):
        pass
    def draw(self, pygame, main_surface):
        pygame.draw.rect(self.surface, self.bgcolor, self.s1_rect)
        pygame.draw.rect(self.surface, self.olcolor, self.s1_rect, 10)
        pygame.draw.rect(self.surface, self.bgcolor, self.s2_rect)
        pygame.draw.rect(self.surface, self.olcolor, self.s2_rect, 10)
        
        main_surface.blit(self.surface, (0,0))