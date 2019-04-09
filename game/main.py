import pygame
import sys
import os
import math

from pygame.locals import K_ESCAPE, K_RETURN, K_w, K_a, K_s, K_d

from ui import UI
from coin import Coin
from constants import *

pygame.init()
pygame.font.init()
pygame.display.set_caption('Money')
window = pygame.display.set_mode(window_dims)
clock = pygame.time.Clock()

# font_big = pygame.font.SysFont('arial.ttf', int(window_dims[1] / 20))
# text_big = font_big.render("GAME JAM", True, (255, 255, 255), background)
# textpos = [window_dims[0] // 2, window_dims[1] // 2]

n_coins = 60
coins = []
for n in range(n_coins):
  coins.append(Coin())

ui = UI(pygame)

i = 0

# GAME EVENT LOOP
game = True
while game:
  i += 1
  if i >= 30: 
    i = 0
    ui.add_money()
  # EVENT LOOP
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == K_ESCAPE:
        sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1: # LEFT CLICK
        ui.handle_event(pygame, event)
        for coin in coins:
          coin.handle_event(pygame, event,ui.player)

  ui.hover_check(pygame.mouse.get_pos())

  pygame.display.flip()
  clock.tick(FPS)
  # DRAW BACKGROUND
  window.fill(background)
  # DRAW COINS
  for coin in coins:
    coin.update()
    window.blit(coin.image,(coin.x,coin.y))
  # DRAW UI
  ui.draw(pygame, window)
