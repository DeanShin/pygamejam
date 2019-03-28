from money_generator import MoneyGenerator as MG
from button import Button as BN

class UI():
    def __init__(self, pygame, num_of_gens):
        self.surface = pygame.Surface((900,600))
        self.font = pygame.font.SysFont('arial.ttf', 20)
        self.bgcolor = (15,15,255)
        self.olcolor = (255,255,255)
        self.rect_sects = []
        self.rect_sects.append((5,5,190,390))
        self.rect_sects.append((5,405,190,190))
        self.gen_rects = []
        for i in range(num_of_gens):
            self.gen_rects.append((10,i*90+10,180,90))
        pass
    def update(self):
        pass
    def draw(self, pygame, main_surface, gens):
        for rect_sect in self.rect_sects:
            pygame.draw.rect(self.surface, self.bgcolor, rect_sect)
            pygame.draw.rect(self.surface, self.olcolor, rect_sect, 10)
        for i, gen_rect in enumerate(self.gen_rects):
            pygame.draw.rect(self.surface, self.olcolor, gen_rect, 2)
            for j, text in enumerate(gens[i].get_text()):
                self.surface.blit(text, (gen_rect[0]+10, gen_rect[1]+30*j+10))
        main_surface.blit(self.surface, (0,0))