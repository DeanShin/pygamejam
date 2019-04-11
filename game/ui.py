from constants import fontpath
from money_generator import MoneyGenerator as MG
from player import Player
from coin import Coin

class UI():
    def __init__(self, pygame):
        self.surface = pygame.Surface((900,600))
        self.surface.set_colorkey((0,0,0))
        font1 = pygame.font.Font(fontpath, 20)
        font2 = pygame.font.Font(fontpath, 40)
        self.bgcolor = (15,15,255)
        self.olcolor = (255,255,255)

        self.main_rects = []
        # Rectangle for the money generators
        self.main_rects.append((5,5,190,390))
        # Rectangle for player information
        self.main_rects.append((5,405,190,190))

        # Money generators
        self.gens = []
        self.gens.append(MG(pygame, 0, font1, "Alan, the Indomitable", 1, 25, "int({}*1.2)//1+1", "{}*2"))
        self.gens.append(MG(pygame, 1, font1, "Blargh, the Yargh", 3, 70, "int({}*1.1)//1+1", "{}*2"))
        self.gens.append(MG(pygame, 2, font1, "C, the Ceaseless", 10, 200, "int({}*1.1)//1+1", "{}*2"))

        # Player information
        self.player = Player(pygame, self.main_rects[1], font2)

        n_coins = 60
        self.coins = []
        for n in range(n_coins):
            self.coins.append(Coin())

    def handle_event(self, pygame, event):
        for gen in self.gens:
            temp = gen.handle_event(pygame, event, self.player.money)
            if temp[0] == 0:
                print(temp)
                print("Insufficient funds!")
            elif temp[0] == 1:
                self.player.update_mps(sum(gen.get_mps() for gen in self.gens))
        for coin in self.coins:
            temp = coin.handle_event(pygame, event)
            if temp == 0:
                self.player.money_isClicked()
    
    def hover_check(self, mouse_pos):
        for gen in self.gens:
            gen.hover_check(mouse_pos)
        pass
    def add_money(self):
        self.player.update_money()

    def draw(self, pygame, sur):
        # DRAW COINS
        for coin in self.coins:
            coin.update()
            sur.blit(coin.image,(coin.x,coin.y))
        for main_rect in self.main_rects:
            pygame.draw.rect(self.surface, self.bgcolor, main_rect)
            pygame.draw.rect(self.surface, self.olcolor, main_rect, 10)
        for gen in self.gens:
            gen.draw(pygame, self.surface)
        self.player.draw(pygame, self.surface)
        sur.blit(self.surface, (0,0))        