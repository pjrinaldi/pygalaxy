import pygame, sys
from pygame.locals import *
import inputbox

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Py64Galaxy')

LIGHTGRAY= (235, 235, 235)
BLACK = (0, 0, 0)

# titleFont = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/CA64v1.ttf', 72)
# titleFont = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_User_v1.0-STYLE.ttf', 68) 
# titleFont = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_User_Mono_v1.0-STYLE.ttf', 60) 
titleFont = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_Pro_v1.0-STYLE.ttf', 60) 
titleText = titleFont.render('PYTHON GALAXY', True, LIGHTGRAY)
titleRect = titleText.get_rect()
titleRect.center = (400, 100)
copyFont = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_Pro_v1.0-STYLE.ttf', 18)
copyText = copyFont.render('COPYRIGHT 2012 PASQUALE J RINALDI JR', True, LIGHTGRAY)
copyRect = copyText.get_rect()
copyRect.center = (400, 300)

'''
startFont = pygame.font.Font(pygame.font.match_font('freesans', False, False), 48)
startText = startFont.render('F1 - Start Single Player Game', True, LIGHTGRAY)
startRect = startText.get_rect()
startRect.center = (400, 200)
'''

gameStart = 0
numPlayers = 0
comPlayers = 0
numWorlds = 0
buildShips = 0

while True: # main game loop
    DISPLAYSURF.blit(titleText, titleRect)
    DISPLAYSURF.blit(copyText, copyRect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        '''
        elif event.type == pygame.KEYUP:
            if(event.key == K_F1):
                playnumText = startFont.render('Enter Number of Players (1-8):', True, LIGHTGRAY)
                playnumRect = playnumText.get_rect()
                playnumRect.center = (400, 300)
                DISPLAYSURF.blit(playnumText, playnumRect)
            if(numPlayers == 0):
                if(event.key >= 49 and event.key <= 56):
                    numPlayers = (event.key - 48)
                    print "Now launch the next line of text questioning user for input."
                    answer = inputbox.ask(DISPLAYSURF, "Number of Worlds (1-26):")
                    #compnumText = startFont.render('Number of Computer Players (1-7):')
            else:
                if(event.key >= 49 and event.key <= 55):
                    comPlayers = (event.key - 48)
                    print "Computer players selected, number of worlds (1-26):"
            if(comPlayers == 0):
                print 'hi'
                # if 1 then nested if 0-9
                # if 2 then nested if 0-9
                # or use the following code below
        '''
    pygame.display.update()