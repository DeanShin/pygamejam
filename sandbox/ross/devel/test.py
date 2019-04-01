
import pygame
import sys
import os
import math

from pygame.locals import K_ESCAPE, K_RETURN, K_w, K_a, K_s, K_d

pygame.init()
pygame.font.init()
pygame.display.set_caption('Money')
window_dims = (900 , 600)
window = pygame.display.set_mode(window_dims)
background = (63,63,63)
FPS = 30.0
clock = pygame.time.Clock()   


font_big = pygame.font.SysFont('arial.ttf', int(window_dims[1] / 20))
text_big = font_big.render("GAME JAM", True, (255, 255, 255), background)
textpos = [window_dims[0] // 2, window_dims[1] // 2]

font_sml = pygame.font.SysFont('arial.ttf', int(window_dims[1] / 30))


''' Add Game Button '''
newBitcoin = pygame.image.load("images/bitcoin_small.png").convert_alpha()


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


  pygame.display.flip()
  clock.tick(FPS)
  # DRAW BACKGROUND
  window.fill(background)
  window.blit(newBitcoin, (0,0))
  # DRAW TEXT
  window.blit(text_big, tuple(textpos))