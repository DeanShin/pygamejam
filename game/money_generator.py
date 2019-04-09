from button import Button

class MoneyGenerator():
    def __init__(self, pygame, id, font, name, mps0, cst0, mgfn = "{}^2", cgfn = "{}**2"):
        self.id = id
        self.rect = pygame.Rect(10,id*90+10,180,90)
        self.font = font

        self.name = name
        self.level = 1
        self.money_per_second = mps0
        self.cost_to_upgrade = cst0
        self.money_growth_func = mgfn
        self.cost_growth_func = cgfn

        ## Name functionless button
        self.name_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+5, 160, 20, False)
        ## Level and MPS functionless button
        self.lvl_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+30, 160, 20, False)
        ## Buy 1 button
        self.buy1_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+55, 50, 20, id=2)
        ## Buy 10 button
        self.buy10_btn = Button(pygame, self.rect[0]+65, self.rect[1]+5+55, 50, 20, id=3)
        ## Buy 100 button
        self.buy100_btn = Button(pygame, self.rect[0]+120, self.rect[1]+5+55, 50, 20, id=4)
        ## Array of buttons
        self.buttons = [self.name_btn,self.lvl_btn,self.buy1_btn,self.buy10_btn,self.buy100_btn]
        self.update_text()

    def update_text(self):
        #RERENDER TEXT
        text0 = self.font.render(self.name, True, (255,255,255))
        self.buttons[0].update_text(text0)
        text1 = self.font.render("Level: {}    MPS: {}".format(self.level, self.money_per_second), True, (255,255,255))
        self.buttons[1].update_text(text1)
        text2 = self.font.render("Buy 1", True, (255,255,255))
        self.buttons[2].update_text(text2)
        text3 = self.font.render("Buy 10", True, (255,255,255))
        self.buttons[3].update_text(text3)
        text4 = self.font.render("Buy 100", True, (255,255,255))
        self.buttons[4].update_text(text4)
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
