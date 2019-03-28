from money_generator import MoneyGenerator as MG
from button import Button as BN

class UI():
    def __init__(self, pygame):
        self.surface = pygame.Surface((900,600))
        self.bgcolor = (15,15,255)
        self.olcolor = (255,255,255)
        self.rect_sects = []
        self.rect_sects.append((5,5,190,390))
        self.rect_sects.append((5,405,190,190))
        self.gens = []
        pass
    def update(self):
        pass
    def draw(self, pygame, main_surface):
        for rect_sect in self.rect_sects:
            pygame.draw.rect(self.surface, self.bgcolor, rect_sect)
            pygame.draw.rect(self.surface, self.olcolor, rect_sect, 10)
        
        main_surface.blit(self.surface, (0,0))