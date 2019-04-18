from constants import fontpath, n_coins
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
        self.gens.append(MG(pygame, 0, font1, "Alan, the Indomitable", 1, 25, "int({}*1.04)//1+1", "{}*1.12//1+1"))
        self.gens.append(MG(pygame, 1, font1, "Blargh, the Yargh", 3, 70, "int({}*1.03)//1+1", "{}*1.23//1"))
        self.gens.append(MG(pygame, 2, font1, "C, the Ceaseless", 10, 200, "int({}*1.03)//1+1", "{}*1.14//1+1"))

        # Player information
        self.player = Player(pygame, self.main_rects[1], font2)

        # n_coins = 60
        self.coins = []
        for n in range(n_coins):
            self.coins.append(Coin())

    def handle_event(self, pygame, event):
        for gen in self.gens:
            temp = gen.handle_event(pygame, event, self.player.money)
            if temp['flag'] == 'insufficient':
                print("Insufficient funds!")
            elif temp['flag'] == 'sufficient':
                self.player.update_mps(sum(gen.get_mps() for gen in self.gens))
                #self.player.money -= temp[1]
                self.player.update_money(temp['cost'],'gen')

        for coin in self.coins:
            temp = coin.handle_event(pygame, event)
            self.player.update_money(temp,'coin')

    def hover_check(self, mouse_pos):
        displayed_something = False
        for gen in self.gens:
            upgrade_cost = gen.hover_check(mouse_pos)
            if upgrade_cost is not False:
                displayed_something = True
                self.player.update_cost(upgrade_cost)
        if not displayed_something:
            self.player.update_cost()

        
    def add_money(self):
        self.player.update_money(False,'gen')

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
