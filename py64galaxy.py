#!/usr/bin/env python

# import statements
import pygame, pygame.locals, random, sys, string

# constant variables
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BACKGROUNDCOLOR = (0, 0, 0)
TEXTCOLOR = (171, 171, 171)
FPS = 40
BLINKER = True
SETUPTEXT = ["HOW MANY PLAYERS (1-20)?", "HOW MANY WORLDS (5-40)?", "HOW MANY YEARS (TURNS) IN THE GAME (1-100)?", "DO YOU WANT THE NEUTRAL WORLDS TO BUILD DEFENSIVE SHIPS?", "NEW SETUP?"]
PLAYERNAMETEXT = ["FLEET ADMIRAL ", " WILL BEGIN THE GAME IN CONTROL OF WORLD:(", ")", "WHAT NAME WILL THIS FLEET ADMIRAL USE (1 TO 8 CHARACTERS)?"]
UNIVERSECREATETEXT = "PLEASE WAIT WHILE I CREATE THE UNIVERSE"
UNIVERSERECREATETEXT = "PLEASE WAIT WHILE I REARRANGE THE STARS"
GAMESETUPTEXT = "NOW WAIT WHILE I SETUP THE GAME"
WORLDLIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "(", ")", "<", ">", "?", "+", "="]
UNIVERSETITLE = "*************** STAR MAP **************"

testString = []
testReturn = ""

# game variables
setupVariables = dict()
# setupVariables = {"numberPlayers": 0, "numberWorlds": 0, "numberTurns": 0, "neutralBuild": -1, "newSetup": 0}
# configureGame = 0
# numberPlayers = 0
# numberWorlds = 0
# numberTurns = 0
# neutralBuild = -1
# newSetup = 0
# playerCount = 1
playerNames = []
worldLocations = dict() # occupied worlds and their locations on the star map
playerWorlds = [] # might not need if i can use worldlist
universeMap = []

# functions
def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def blinkInputCursor(isBlink, surface, x, y):
        textobj = font.render(" ", 1, TEXTCOLOR, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        isBlink = not isBlink
        if isBlink:
            surface.blit(textobj, textrect)
        pygame.display.update(textrect)
        pygame.time.wait(500)
        return isBlink

def waitForKeyPress():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                terminate()
            if event.type == pygame.locals.KEYUP:
                if event.key == pygame.locals.K_ESCAPE: # pressing escape quits
                    terminate()
                return

def waitForReturn(tmpString):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.KEYUP:
                if event.key == pygame.locals.K_BACKSPACE:
                    tmpString = tmpString[0:-1]
                elif event.key == pygame.locals.K_RETURN:
                    return string.join(tmpString, "")
                elif event.key <= 127:
                    tmpString.append(chr(event.key))
            
def collectInput(tmpString):
    tmpCharArray = []
    # BEGIN LOOP SEQUENCE TO COLLECT GAME SETUP INFORAMTION
    windowSurface.fill(BACKGROUNDCOLOR)
    drawText(tmpString, font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    pygame.display.update()
    return waitForReturn(tmpCharArray)
    

# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
blinkClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Py64Galaxy')
pygame.mouse.set_visible(False)

# set up fonts
font = pygame.font.Font("./resources/C64_Pro_Mono_v1.0-STYLE.ttf", 12)

# set up sounds
# gameOverSound = pygame.mixer.Sound('gameover.wav')
# pygame.mixer.music.load('background.mid')

# set up images
# playerImage = pygame.image.load('player.png')
# playerRect = playerImage.get_rect()
# baddieImage = pygame.image.load('baddie.png')

# show the "Start" screen
drawText('Python Galaxy', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForKeyPress()
while True:
    # collect setup information
    # BLINKER = blinkInputCursor(BLINKER, windowSurface, 10, 10)
    # blinkClock.tick(FPS)
    setupVariables["numberPlayers"] = collectInput(SETUPTEXT[0])
    # BLINKER = blinkInputCursor(BLINKER, windowSurface, 10, 10)
    # blinkClock.tick(FPS)
    print setupVariables
    setupVariables["numberWorlds"] = collectInput(SETUPTEXT[1])
    print setupVariables
    break

# Game Loop
while True:
    # CREATE A FUNCTION FOR STARTER INFORMATION.  COLLECTINFO(INCREMENT)
    # AS I COLLECT INFO, INCREMENT THE VALUE OF INCREMENT AND USE THAT TO DISPLAY THE VARIOUS TEXT AND RECEIVE INPUTS FROM USER
    # THEN I CAN GET INTO THE GAME LOOP, ONCE I COLLECT THE REQUIRED INFORMATION
    
    windowSurface.fill(BACKGROUNDCOLOR)
    drawText('TURN 1 CYCLE', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    # drawText('Enter Text: ', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    BLINKER = blinkInputCursor(BLINKER, windowSurface, 10, 10)
    # testString = waitForReturn(testString)
    # print testString
    
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            terminate()
        
        if event.type == pygame.locals.KEYUP:
            if event.key == pygame.locals.K_ESCAPE:
                terminate()
    
    pygame.display.update()
    mainClock.tick(FPS)

'''
# From Statements

# Import Statements
import wx
import GalaxyFrame

#
# Main Application Class      
# Launch MainWindow  
class GalaxyApp(wx.App):
    def OnInit(self):
        frame = GalaxyFrame.GalaxyFrame(None, "Python Galaxy!")
        self.SetTopWindow(frame)
        # frame.SetIcon(wx.Icon("images/wombat_32.ico", wx.BITMAP_TYPE_ICO, 32, 32))
        frame.Show(True)
        frame.SetFocus()
        return True

# Create Main Application and Run It
app = GalaxyApp(redirect=False)
app.MainLoop()
'''

'''
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
    screen.blit(tmpText, tmpRect)
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
    gameStart = 1 # bypasses old and new game
    gameType = 2 # sets it to a new game automatically
    numPlayers = 0
    comPlayers = 0
    numWorlds = 0
    buildShips = 0
    LIGHTGRAY= (235, 235, 235)    

#Main Loop
    while 1:
        clock.tick(60)

    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYUP:
                if(gameStart == 1):
                    if(gameType == 0):
                        if(event.key == K_o):
                            gameType = 1 # old game
                            print 'old game'
                        elif (event.key == K_n):
                            gameType = 2 # new game
                            print 'new game'
                    if(gameType == 1):
                        print 'figure out how to load an old game much later'
                        
            elif event.type == MOUSEBUTTONDOWN:
                if(gameStart == 0):
                    gameStart = 1
                    background.fill((0, 0, 0))
                    if pygame.font:
                        mainFont = pygame.font.Font('/home/pasquale/projects/py64galaxy/resources/C64_Pro_v1.0-STYLE.ttf', 12)
                        text= mainFont.render('DO YOU WANT TO RETURN TO AN OLD GAME (O) OR START A NEW(N) ONE?', True, LIGHTGRAY)
                        textRect = text.get_rect()
                        textRect.center = (400, 200)
                        background.blit(text, textRect)
                        screen.blit(background, (0, 0))
                elif(gameStart == 1):
                    print 'capture and do nothing with - maybe pause later on'
        # allsprites.update()

    #Draw Everything
        screen.blit(background, (0, 0))
        # allsprites.draw(screen)
        pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
'''