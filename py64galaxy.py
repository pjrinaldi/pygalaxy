import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Py64Galaxy')

LIGHTGRAY= (235, 235, 235)
BLACK = (0, 0, 0)

titleFont = pygame.font.Font(pygame.font.match_font('freesans', False, False), 72) 
titleText = titleFont.render('Python Galaxy', True, LIGHTGRAY)
titleRect = titleText.get_rect()
titleRect.center = (400, 100)
startFont = pygame.font.Font(pygame.font.match_font('freesans', False, False), 48)
startText = startFont.render('F1 - Start Single Player Game', True, LIGHTGRAY)
startRect = startText.get_rect()
startRect.center = (400, 200)

while True: # main game loop
    DISPLAYSURF.blit(titleText, titleRect)
    DISPLAYSURF.blit(startText, startRect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if(event.key == K_F1):
                playnumText = startFont.render('Enter Number of Players (1-8):', True, LIGHTGRAY)
                playnumRect = playnumText.get_rect()
                playnumRect.center = (400, 300)
                DISPLAYSURF.blit(playnumText, playnumRect)
                print 'start game here by prompting for number of players'
    pygame.display.update()
