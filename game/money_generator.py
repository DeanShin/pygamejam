class MoneyGenerator():
    def __init__(self, name, mps0, cst0, mgfn = "{}^2", cgfn = "{}**2"):
        self.name = ""
        self.level = 1
        self.money_per_second = mps0
        self.cost_to_upgrade = cst0
        self.money_growth_func = mgfn
        self.cost_growth_func = cgfn
    def level_up(self):
        self.level += 1
        self.money_per_second = \
            eval(self.money_growth_func.format(self.money_per_second))
        self.cost_to_upgrade = \
            eval(self.cost_growth_func.format(self.cost_to_upgrade))
    def get_money(self):
        return self.money_per_second
    def get_cost(self):
        return self.cost_to_upgrade
    def get_cost_mult(self, n):
        #UNTESTED
        cost = 0
        temp = self.cost_to_upgrade
        for i in range(n):
            cost += temp
            temp = eval(self.cost_growth_func.format(temp))
        return cost            

        