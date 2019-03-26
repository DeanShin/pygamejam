class MoneyGenerator():
    def __init__(self, font, name, mps0, cst0, mgfn = "{}^2", cgfn = "{}**2"):
        self.font = font
        self.name = ""
        self.level = 1
        self.money_per_second = mps0
        self.cost_to_upgrade = cst0
        self.money_growth_func = mgfn
        self.cost_growth_func = cgfn
        self.text = self.font.render("Level: {}".format(self.level), \
            True, (255,255,255))
    def update(self):
        #RERENDER TEXT
        self.text = self.font.render("Level: {}".format(self.level), \
            True, (255,255,255))
    def level_up(self):
        self.level += 1
        self.money_per_second = \
            eval(self.money_growth_func.format(self.money_per_second))
        self.cost_to_upgrade = \
            eval(self.cost_growth_func.format(self.cost_to_upgrade))
        self.update()
    def get_money(self):
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
    def draw(self, window):
        window.blit(self.text, (0, 0))

    
