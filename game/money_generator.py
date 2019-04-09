from button import Button
import time

class MoneyGenerator():
    def __init__(self, pygame, id, font, name, mps0, cst0, mgfn = "{}^2", cgfn = "{}**2"):
        self.id = id
        self.rect = pygame.Rect(10,id*90+10,180,90)
        self.font = font
        self.money = 0
        self.name = name
        self.level = 1
        self.money_per_second = mps0
        self.cost_to_upgrade = cst0
        self.money_growth_func = mgfn
        self.cost_growth_func = cgfn

   
        
        #name
        self.name_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+5, 160, 20, False)
        
        #level, mps
        self.lvl_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+30, 160, 20, False)
        
        #buy 1
        self.buyone_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+55, 50, 20, id=2)
        
        #buy 10
        self.buyten_btn = Button(pygame, self.rect[0]+65, self.rect[1]+5+55, 50, 20, id=3)

        
        #buy 100
        self.buyhundo_btn = Button(pygame, self.rect[0]+120, self.rect[1]+5+55, 50, 20, id=4)
        
        self.buttons = [self.name_btn,self.lvl_btn,self.buyone_btn,self.buyten_btn,self.buyhundo_btn]

        self.update_text()

    def update_text(self):
        #RERENDER TEXT
        text0 = self.font.render('{}'.format(self.name), True, (255,255,255))
        self.name_btn.update_text(text0)
        text1 = self.font.render("Level: {}    MPS: {}".format(self.level, self.money_per_second), True, (255,255,255))
        self.lvl_btn.update_text(text1)
        text2 = self.font.render("Buy 1", True, (255,255,255))
        self.buyone_btn.update_text(text2)
        text3 = self.font.render("Buy 10", True, (255,255,255))
        self.buyten_btn.update_text(text3)
        text4 = self.font.render("Buy 100", True, (255,255,255))
        self.buyhundo_btn.update_text(text4)
        
    def level_up(self, n=1):
        self.level += 1
        self.money_per_second = \
            eval(self.money_growth_func.format(self.money_per_second))
        self.cost_to_upgrade = \
            eval(self.cost_growth_func.format(self.cost_to_upgrade))
        n -= 1
        print(n)
        if n > 0: self.level_up(n)
        else: self.update_text()

    def handle_event(self, pygame, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            for button in self.buttons:
                id = button.handle_event(pygame, event)
                if id == 2: self.level_up()
                elif id == 3: self.level_up(10)
                elif id == 4: self.level_up(100)
            
    def hover_check(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            for button in self.buttons:
                button.hover_check(mouse_pos)
    def get_money(self):
        self.money+=self.get_mps()
        return self.money

   
    def draw(self, pygame, sur):
        pygame.draw.rect(sur, (255,255,255), self.rect, 2)
        for button in self.buttons:
            button.draw(pygame, sur)

    def get_mps(self):
        return self.money_per_second
  
    def get_cost(self):
        return self.cost_to_upgrade
  

    def get_cost_mult(self, n):
        cost = 0
        temp = self.cost_to_upgrade
        for i in range(n):
            cost += temp
            temp = eval(self.cost_growth_func.format(temp))
        return cost
