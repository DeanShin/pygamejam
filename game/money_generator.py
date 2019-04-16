from button import Button
from global_functions import *

class MoneyGenerator():
    def __init__(self, pygame, button_id, font, name, mps0, cst0, mgfn = "{}^2", cgfn = "{}**2"):
        self.button_id = button_id
        self.rect = pygame.Rect(10,button_id*90+10,180,90)
        self.font = font

        self.name = name
        self.level = 1
        self.money_per_second = mps0
        self.cost_to_upgrade = cst0
        self.money_growth_func = mgfn
        self.cost_growth_func = cgfn

        ## Name button (funcctionless)
        self.name_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+5, 160, 20, False)
        ## Level and MPS button (functionless)
        self.lvl_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+30, 160, 20, False)
        ## Buy 1 button
        self.buy1_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+55, 50, 20, button_id=2)
        ## Buy 10 button
        self.buy10_btn = Button(pygame, self.rect[0]+65, self.rect[1]+5+55, 50, 20, button_id=3)
        ## Buy 100 button
        self.buy100_btn = Button(pygame, self.rect[0]+120, self.rect[1]+5+55, 50, 20, button_id=4)
        ## Array of buttons
        self.buttons = [self.name_btn,self.lvl_btn,self.buy1_btn,self.buy10_btn,self.buy100_btn]
        self.update_text()

    def update_text(self):
        #RERENDER TEXT
        text0 = self.font.render(self.name, True, (255,255,255))
        self.buttons[0].update_text(text0)
        text1 = self.font.render("Level: {}    MPS: {}".format(self.level, format_int(self.money_per_second)), True, (255,255,255))
        self.buttons[1].update_text(text1)
        text2 = self.font.render("Buy 1", True, (255,255,255))
        self.buttons[2].update_text(text2)
        text3 = self.font.render("Buy 10", True, (255,255,255))
        self.buttons[3].update_text(text3)
        text4 = self.font.render("Buy 100", True, (255,255,255))
        self.buttons[4].update_text(text4)
    def level_up(self, n=1):
        self.level += 1
        ## Increase the money per second produced by the money generator.
        self.money_per_second = \
            eval(self.money_growth_func.format(self.money_per_second))
        ## Increase the money required to level up the money generator.
        self.cost_to_upgrade = \
            eval(self.cost_growth_func.format(self.cost_to_upgrade))
        #print(n)
        ## Recursion
        n -= 1
        if n > 0: self.level_up(n)
        ## When done leveling up, make text up to date with new information.
        else:
            self.update_text()

    def handle_event(self, pygame, event, player_funds):
        temp = [-1, 0] # Temp[0] = -1 if no button is clicked or button has no function
        if self.rect.collidepoint(event.pos):
            for button in self.buttons:
                button_id = button.handle_event(pygame, event)
                if button_id != -1:
                    temp = [0, 0] # Temp[0] = 0 if not enough money to purchase money gen
                    if button_id == 2:
                        temp[1] = self.get_cost(1)
                        if player_funds >= temp[1]:
                            self.level_up(1)
                            temp[0] = 1
                        return temp
                    elif button_id == 3:
                        temp[1] = self.get_cost(10)
                        if player_funds >= temp[1]:
                            self.level_up(10)
                            temp[0] = 1
                        return temp
                    elif button_id == 4:
                        temp[1] = self.get_cost(100)
                        if player_funds >= temp[1]:
                            self.level_up(100)
                            temp[0] = 1
                        return temp
        return temp

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
    # def get_cost(self):
    #     return self.cost_to_upgrade
    def get_cost(self, n):
        cost = 0
        temp = self.cost_to_upgrade
        for i in range(n):
            cost += temp
            temp = eval(self.cost_growth_func.format(temp))
        return cost
