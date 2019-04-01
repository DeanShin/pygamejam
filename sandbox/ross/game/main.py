import pygame
import sys
import os
import math

from pygame.locals import K_ESCAPE, K_RETURN, K_w, K_a, K_s, K_d

from ui import UI
from button import Button as BN
from money_generator import MoneyGenerator as MG
from pprint import pprint
from coin import Coin

from constants import *

pygame.init()
pygame.font.init()
pygame.display.set_caption('Money')
# window_dims = (900 , 600)
# width = window_dims[0]
# height = window_dims[1]

window = pygame.display.set_mode(window_dims)
background = (63,63,63)
FPS = 30.0
clock = pygame.time.Clock()   

fontpath = "./resources/Dosis-Regular.ttf"

font_big = pygame.font.SysFont('arial.ttf', int(window_dims[1] / 20))
text_big = font_big.render("GAME JAM", True, (255, 255, 255), background)
textpos = [window_dims[0] // 2, window_dims[1] // 2]

font_sml = pygame.font.SysFont('arial.ttf', int(window_dims[1] / 30))

gens = []
gens.append(MG(pygame, 0, font_sml, "Alan, the Indomitable", 1, 25, "({}*2)//1+1", "{}*2"))
gens.append(MG(pygame, 1, font_sml, "Blargh, the Yargh", 3, 70, "({}*2)//1+1", "{}*2"))
gens.append(MG(pygame, 2, font_sml, "C, the Ceaseless", 10, 200, "({}*2)//1+1", "{}*2"))
gens.append(MG(pygame, 2, font_sml, "Darth, son of Barth", 7, 10, "({}*2)//1+1", "{}*2"))
print(len(gens))
ui = UI(pygame)
# GAME EVENT LOOP
game = True

''' Add Coins to Game '''
coins = []
for n in range(n_coins):
  coins.append(Coin())

while game:
  # EVENT LOOP
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == K_ESCAPE:
        sys.exit()
      if event.key == K_w:
        textpos[1]-=10
      if event.key == K_a:
        textpos[0]-=10
      if event.key == K_s:
        textpos[1]+=10
      if event.key == K_d:
        textpos[0]+=10
        for gen in gens:
          gen.level_up()
    if event.type == pygame.MOUSEBUTTONDOWN:
      ui.handle_event(gens, pygame, event)

  ui.hover_check(gens, pygame.mouse.get_pos())

  pygame.display.flip()
  clock.tick(FPS)
  # DRAW BACKGROUND
  window.fill(background)
  # DRAW TEXT
  window.blit(text_big, tuple(textpos))

  # DRAW UI
  ui.draw(pygame, window, gens)

  # DRAW Coins
  for coin in coins:
    coin.update()
    window.blit(coin.image,(coin.x,coin.y))