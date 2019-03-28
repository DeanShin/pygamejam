import pygame
import sys
import os
import math

from pygame.locals import K_ESCAPE, K_RETURN, K_w, K_a, K_s, K_d

from ui import UI
from button import Button as BN
from money_generator import MoneyGenerator as MG


pygame.init()
pygame.font.init()
pygame.display.set_caption('Money')
window_dims = (900 , 600)
window = pygame.display.set_mode(window_dims)
background = (63,63,63)
FPS = 30.0
clock = pygame.time.Clock()   

fontpath = "./resources/Dosis-Regular.ttf"

font_big = pygame.font.SysFont('arial.ttf', int(window_dims[1] / 20))
text_big = font_big.render("GAME JAM", True, (255, 255, 255), background)
textpos = [window_dims[0] // 2, window_dims[1] // 2]

font_sml = pygame.font.SysFont('arial.ttf', int(window_dims[1] / 40))

gens = []
gens.append(MG(font_sml, "A", 1, 25, "({}*2)//1+1", "{}*2"))

game_ui = UI(pygame)
# GAME EVENT LOOP
game = True
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
        gen1.level_up()
      
  pygame.display.flip()
  clock.tick(FPS)
  # DRAW BACKGROUND
  window.fill(background)
  # DRAW TEXT
  window.blit(text_big, tuple(textpos))
  # DRAW UI
  game_ui.draw(pygame, window)