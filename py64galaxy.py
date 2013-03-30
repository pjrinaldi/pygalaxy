#!/usr/bin/env python

# import statements
import pygame, random, sys

# from statements
from pygame.locals import *

# constant variables
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BACKGROUNDCOLOR = (0, 0, 0)
TEXTCOLOR = (171, 171, 171)
FPS = 40

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


pygame.init()
'''
    self.titleFont = ImageFont.truetype("./resources/C64_Pro_Mono_v1.0-STYLE.ttf", 48)
    self.gameFont = ImageFont.truetype("./resources/C64_Pro_Mono_v1.0-STYLE.ttf", 12)
    self.keyStrokesList = []
    self.titleText = "PYTHON GALAXY!"
    self.numPlayerText = "HOW MANY PLAYERS (1-20)?"
    self.numWorldsText = "HOW MANY WORLDS (5-40)?"
    self.numTurnsText = "HOW MANY YEARS (TURNS) IN THE GAME (1-100)?"
    self.neutralBuildText = "DO YOU WANT THE NEUTRAL WORLDS TO BUILD DEFENSIVE SHIPS?"
    self.playerNameText = ["FLEET ADMIRAL ", " WILL BEGIN THE GAME IN CONTROL OF WORLD:(", ")", "WHAT NAME WILL THIS FLEET ADMIRAL USE (1 TO 8 CHARACTERS)?"]
    self.universeCreateText = "PLEASE WAIT WHILE I CREATE THE UNIVERSE"
    self.askNewSetupText = "NEW SETUP?"
    self.universeReCreateText = "PLEASE WAIT WHILE I REARRANGE THE STARS"
    self.gameSetupText = "NOW WAIT WHILE I SETUP THE GAME"
    self.worldList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "(", ")", "<", ">", "?", "+", "="]
    self.configureGame = 0
    self.numPlayers = 0
    self.numWorlds = 0
    self.numTurns = 0
    self.neutralBuild = -1
    self.newSetup = 0
    self.playerCount = 1
    self.playerNames = []
    self.worldLocations = dict() # occupied worlds and their locations on the star map
    self.playerWorlds = [] # might not need if i cna just use worldlist
    self.universeTitle = "*************** STAR MAP **************"
    self.universeMap = []
'''

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