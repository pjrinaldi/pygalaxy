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

numPlayers = 0
comPlayers = 0

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
            if(numPlayers == 0):
                if(event.key >= 49 and event.key <= 56):
                    numPlayers = (event.key - 48)
                    print "Now launch the next line of text questioning user for input."
                    compnumText = startFont.render('Number of Computer Players (1-7):')
            else:
                if(event.key >= 49 and event.key <= 55):
                    comPlayers = (event.key - 48)
                    print "Computer players selected, number of worlds (1-26):"
            if(comPlayers == 0):
                # if 1 then nested if 0-9
                # if 2 then nested if 0-9
                # or use the following code below
    pygame.display.update()
'''
# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

def main():
  screen = pygame.display.set_mode((320,240))
  print ask(screen, "Name") + " was entered"

if __name__ == '__main__': main()
'''
