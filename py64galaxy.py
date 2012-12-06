import pygame, os, sys, string
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def  get_key():
    while 1:
        event = pygame.event.poll()
        if(event.type == KEYDOWN):
            return event.key
        else:
            pass
        
def ask(screen, question):
    tmpFont = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_Pro_v1.0-STYLE.ttf', 12)
    tmpText = tmpFont.render(question, True, (235, 235, 235))
    tmpRect = tmpText.get_rect()
    tmpRect.center = (400, 200)
    current_string = []
    screen.blit(tmpText + " " + current_string, tmpRect)
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
            
            return string.join(current_string,"")

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Python Galaxy!')
    pygame.mouse.set_visible(0)

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

#Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_Pro_v1.0-STYLE.ttf', 48)
        text = font.render("Python Galaxy!", True, (235, 235, 235))
        textpos = text.get_rect(center=(background.get_width()/2, background.get_height()/4))
        background.blit(text, textpos)
        font = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_Pro_v1.0-STYLE.ttf', 16)
        text = font.render('COPYRIGHT 2012 PASQUALE J RINALDI JR', True, (235, 235, 235))
        textpos = text.get_rect(center=(background.get_width()/2, background.get_height()/2))
        background.blit(text, textpos)

#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

#Prepare Game Objects
    clock = pygame.time.Clock()
    # whiff_sound = load_sound('whiff.wav')
    # punch_sound = load_sound('punch.wav')
    # chimp = Chimp()
    # fist = Fist()
    # allsprites = pygame.sprite.RenderPlain((fist, chimp))

#Main Loop
    while 1:
        clock.tick(60)

    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                '''
                if fist.punch(chimp):
                    punch_sound.play() #punch
                    chimp.punched()
                else:
                    whiff_sound.play() #miss
            elif event.type is MOUSEBUTTONUP:
                fist.unpunch()
                '''

        # allsprites.update()

    #Draw Everything
        screen.blit(background, (0, 0))
        # allsprites.draw(screen)
        pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()


'''
#/usr/bin/env python
"""
This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation, 
follow along in the tutorial.
"""


#Import Modules
import os, pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


#functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound


#classes for our game objects
class Fist(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('fist.bmp', -1)
        self.punching = 0

    def update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5, 10)

    def punch(self, target):
        "returns true if the fist collides with the target"
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        "called to pull the fist back"
        self.punching = 0


class Chimp(pygame.sprite.Sprite):
    """moves a monkey critter across the screen. it can spin the
       monkey when it is punched."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image('chimp.bmp', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9
        self.dizzy = 0

    def update(self):
        "walk or spin, depending on the monkeys state"
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        "move the monkey across the screen, and turn at the ends"
        newpos = self.rect.move((self.move, 0))
        if self.rect.left < self.area.left or \
           self.rect.right > self.area.right:
            self.move = -self.move
            newpos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos

    def _spin(self):
        "spin the monkey image"
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        "this will cause the monkey to start spinning"
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((468, 60))
    pygame.display.set_caption('Monkey Fever')
    pygame.mouse.set_visible(0)

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

#Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

#Prepare Game Objects
    clock = pygame.time.Clock()
    whiff_sound = load_sound('whiff.wav')
    punch_sound = load_sound('punch.wav')
    chimp = Chimp()
    fist = Fist()
    allsprites = pygame.sprite.RenderPlain((fist, chimp))

#Main Loop
    while 1:
        clock.tick(60)

    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play() #punch
                    chimp.punched()
                else:
                    whiff_sound.play() #miss
            elif event.type is MOUSEBUTTONUP:
                fist.unpunch()

        allsprites.update()

    #Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
'''
'''
pygame.init()
mainscreen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Py64Galaxy')

LIGHTGRAY= (235, 235, 235)
BLACK = (0, 0, 0)
gameClock = pygame.time.Clock()


titleFont = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_Pro_v1.0-STYLE.ttf', 48) 
copyFont = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_Pro_v1.0-STYLE.ttf', 16)
gameFont = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_Pro_v1.0-STYLE.ttf', 12)
titleText = titleFont.render('PYTHON GALAXY', True, LIGHTGRAY)
titleRect = titleText.get_rect()
titleRect.center = (400, 100)
copyText = copyFont.render('COPYRIGHT 2012 PASQUALE J RINALDI JR', True, LIGHTGRAY)
copyRect = copyText.get_rect()
copyRect.center = (400, 300)

gameStart = 0
gameType = 0
numPlayers = 0
comPlayers = 0
numWorlds = 0
buildShips = 0

while True:
    mainscreen.blit(titleText, titleRect)
    mainscreen.blit(copyText, copyRect)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if(event.type == pygame.KEYUP):
            gameStart = 1
            mainscreen.fill((0, 0, 0), None, 0)
            answer = pygame.ask(mainscreen, "DO YOU WANT TO RETURN TO AN OLD GAME (O) OR START A NEW(N) ONE?")
'''

'''
while True: # main game loop
    # gameClock.tick(50)
    mainscreen.blit(titleText, titleRect)
    mainscreen.blit(copyText, copyRect)
    # print gameStart
    # pygame.display.update()
    # pygame.time.wait(3000)
    # mainscreen.fill((0, 0, 0), None, 0)
    # pygame.display.update()
    # gameText = gameFont.render('DO YOU WANT TO RETURN TO AN OLD GAME (O) OR START A NEW(N) ONE?', True, LIGHTGRAY)
    # gameRect = gameText.get_rect()
    # gameRect.center = (400, 200)
    # mainscreen.blit(gameText, gameRect)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif(gameStart == 0 and event.type == pygame.KEYUP):
            gameStart = 1
            mainscreen.fill((0, 0, 0), None, 0)
            answer = inputbox.ask(mainscreen, "DO YOU WANT TO RETURN TO AN OLD GAME (O) OR START A NEW(N) ONE?")
            print gameStart
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
    pygame.display.update()
'''