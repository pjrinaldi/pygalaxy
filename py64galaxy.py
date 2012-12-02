import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Py64Galaxy')

LIGHTGRAY= (235, 235, 235)
BLACK = (0, 0, 0)

titleFont = pygame.font.Font('freesansbold.ttf', 32)
titleText = titleFont.render('Python Galaxy', True, LIGHTGRAY)
titleRect = titleText.get_rect()
titleRect.center = (200, 50)

while True: # main game loop
    DISPLAYSURF.blit(titleText, titleRect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
