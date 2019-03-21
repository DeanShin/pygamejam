import pygame
import sys
import os
from pygame.locals import K_ESCAPE, K_RETURN, K_w, K_a, K_s, K_d


pygame.init()
pygame.font.init()         
print(pygame.font.get_fonts())
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
# GAME EVENT LOOP
game = True
while game:
  #event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game = False
    if event.type == pygame.KEYDOWN:
      if event.key == K_w:
        textpos[1]-=10
      if event.key == K_a:
        textpos[0]-=10
      if event.key == K_s:
        textpos[1]+=10
      if event.key == K_d:
        textpos[0]+=10

  # Draw the background
  pygame.display.flip()
  clock.tick(FPS)
  window.fill(background)
  window.blit(text_big, tuple(textpos))
