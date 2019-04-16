from constants import *
from button import Button
from global_functions import *
class Player():
    def __init__(self, pygame, rect, font):
        self.rect = rect
        self.font = font

        self.mps = 1
        self.mpc = 1
        self.money = 0

        self.name_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+5, 160, 30, False)
        self.mps_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+35, 160, 30, False)
        self.mpc_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+65, 160, 30, False)
        self.money_btn = Button(pygame, self.rect[0]+10, self.rect[1]+5+95, 160, 30, False)
        self.buttons = (self.name_btn,self.mps_btn,self.mpc_btn,self.money_btn)
        self.update_text()

    def update_text(self):
        #RERENDER TEXT
        text0 = self.font.render("Clicker", True, (255,255,255))
        self.buttons[0].update_text(text0)
        self.update_mps(0)
        text2 = self.font.render("MPC: {}".format(format_int(self.mpc)), True, (255,255,255))
        self.buttons[2].update_text(text2)
        self.update_money(None,None)

    def update_mps(self, mps_sum):
        self.mps = mps_sum
        text1 = self.font.render("MPS: {}".format(format_int(mps_sum)), True, (255,255,255))
        self.buttons[1].update_text(text1)

    def update_money(self, money, type):
        # if money is None: # do nothing
        #     pass
        # elif money is -1: # -1 is money generator
        #     self.money += self.mps
        # elif money==0: # 0 is money click
        #     self.money += self.mpc
        # else: # any other value is money spent
        #     self.money -= money

        if money is None: # do nothing
            pass
        elif type is 'gen': # -1 is money generator
            self.money += self.mps
        elif type is 'coin': # 0 is money click
            self.money += money
        else: # any other value is money spent
            self.money -= money
        text3 = self.font.render("${}".format(format_int(self.money)), True, (255,255,255))
        self.buttons[3].update_text(text3)

    def draw(self, pygame, sur):
        for button in self.buttons:
            button.draw(pygame, sur)
