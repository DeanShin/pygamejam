class MoneyGenerator():
    def __init__(self, font, name, mps0, cst0, mgfn = "{}^2", cgfn = "{}**2"):
        self.font = font
        self.name = name
        self.level = 1
        self.money_per_second = mps0
        self.cost_to_upgrade = cst0
        self.money_growth_func = mgfn
        self.cost_growth_func = cgfn
        self.render_text()
    def render_text(self):
        #RERENDER TEXT
        self.text1 = self.font.render(self.name, \
            True, (255,255,255))
        self.text2 = self.font.render("Level: {}    MPS: {}".format(self.level, self.money_per_second), \
            True, (255,255,255))
    def level_up(self):
        self.level += 1
        self.money_per_second = \
            eval(self.money_growth_func.format(self.money_per_second))
        self.cost_to_upgrade = \
            eval(self.cost_growth_func.format(self.cost_to_upgrade))
        self.render_text()
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
    def get_text(self):
        return (self.text1, self.text2)