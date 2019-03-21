import pygame
from pygame.locals import K_ESCAPE, K_RETURN, K_w, K_a, K_s, K_d


pygame.init()
pygame.font.init()
pygame.display.set_caption('Money')
window_dims = (1760, 990)
window = pygame.display.set_mode(window_dims)
background = (63,63,63)
FPS = 30.0
clock = pygame.time.Clock()

fontpath = "./Dosis-Regular.ttf"

font_big = pygame.font.Font(fontpath, int(window_dims[1] / 9))
text_big = font_big.render("Something", True, (255, 255, 255), background)

# GAME EVENT LOOP

while True:
    pygame.display.flip()
    window.fill(background)
    window.blit(text_big,(63,63))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    pygame.display.update()
    clock.tick(FPS)
