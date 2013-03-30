from wx import wx
from PIL import Image, ImageFont, ImageDraw
import time
import random

class GalaxyFrame(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.imageViewer = wx.Panel(self, style=wx.BORDER_NONE)
        self.imageViewer.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.imageViewer.Bind(wx.EVT_CHAR, self.CaptureKeys)
        self.mainBox = wx.BoxSizer(wx.VERTICAL)
        self.mainBox.Add(self.imageViewer, 1, wx.ALL | wx.EXPAND | wx.ALIGN_LEFT)
        self.SetSizer(self.mainBox)
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
        self.mainImage = Image.new('L', self.GetSize())
        self.mainDraw = ImageDraw.Draw(self.mainImage)
        self.AddTitleText(self.titleText)
        self.wxBmp = wx.EmptyBitmap(self.GetSize()[0], self.GetSize()[1])
        self.mainBmp = wx.StaticBitmap(self.imageViewer, -1, self.wxBmp, wx.Point(0, 0))
        self.BlitTextSurface()
                
        self.Show(True)
    def CaptureKeys(self, event):
        keycode = event.GetKeyCode()
        if self.configureGame == 0: # ask for number of players.
            self.keyStrokesList = []
            self.configureGame = 1
            self.AddText(self.numPlayerText, 0)
            self.BlitTextSurface()
        elif self.configureGame == 1: # ask for the number of worlds.
            if keycode > 47 and keycode < 58:
                self.keyStrokesList.append(keycode - 48)
            elif keycode == 13:
                testNum = ""
                for i in self.keyStrokesList:
                    testNum = testNum + str(i)
                if testNum.isdigit():
                    if int(testNum) > 0 and int(testNum) < 21:                    
                        self.configureGame = 2
                        self.numPlayers = int(testNum)
                        self.numPlayerText = self.numPlayerText + " " + testNum
                        self.keyStrokesList = []
                        self.AddText(self.numPlayerText, 0)
                        self.AddText(self.numWorldsText, 1)
                        self.BlitTextSurface()
                    else:
                        self.configureGame = 1
                        self.keyStrokesList = []
                        self.BlinkSurface()
                else:
                    self.BlinkSurface()
                    self.keyStrokesList = []
        elif self.configureGame == 2: # ask for the number of turns.
            if keycode > 47 and keycode < 58: # number 1 thru 0 pressed
                self.keyStrokesList.append(keycode - 48)
            elif keycode == 13: # return pressed
                testNum = ""
                for i in self.keyStrokesList:
                    testNum = testNum + str(i)
                if testNum.isdigit(): # if captured keystrokes were a valid number
                    if int(testNum) > 4 and int(testNum) < 41: # if its between world range
                        self.configureGame = 3
                        self.numWorlds = int(testNum)
                        self.numWorldsText = self.numWorldsText + " " + testNum
                        self.keyStrokesList = []
                        self.AddText(self.numPlayerText, 0)
                        self.AddText(self.numWorldsText, 1)
                        self.AddText(self.numTurnsText, 2)
                        self.BlitTextSurface()
                    else:
                        self.configureGame = 2
                        self.keyStrokesList = []
                        self.BlinkSurface()
                else:
                    self.BlinkSurface()
                    self.keyStrokesList = []
        elif self.configureGame == 3: # ask for neutral build
            if keycode > 47 and keycode < 58: # number 1 thru 0 pressed
                self.keyStrokesList.append(keycode - 48)
            elif keycode == 13: # return pressed
                testNum = ""
                for i in self.keyStrokesList:
                    testNum = testNum + str(i)
                if testNum.isdigit(): # if captured keystrokes were a valid number
                    if int(testNum) > 0 and int(testNum)< 101: # if its between years range
                        self.configureGame = 4
                        self.numTurns = int(testNum)
                        self.numTurnsText = self.numTurnsText + " " + testNum
                        self.keyStrokesList = []
                        self.AddText(self.numPlayerText, 0)
                        self.AddText(self.numWorldsText, 1)
                        self.AddText(self.numTurnsText, 2)
                        self.AddText(self.neutralBuildText, 3)
                        self.BlitTextSurface()
                    else:
                        self.configureGame = 3
                        self.keyStrokesList = []
                        self.BlinkSurface()
                else:
                    self.BlinkSurface()
                    self.keyStrokesList = []
        elif self.configureGame == 4: # ask for playername(s)
            if keycode == 121 or keycode == 89 or keycode == 110 or keycode == 78: # y Y n N
                if keycode == 121 or keycode == 89:
                    self.neutralBuild = 1
                else:
                    self.neutralBuild= 0
                self.configureGame = 5
                self.AddText(''.join([self.playerNameText[0], str(self.playerCount), self.playerNameText[1], self.worldList[self.playerCount - 1], self.playerNameText[2]]), 0)
                self.AddText(self.playerNameText[3], 1)
                self.BlitTextSurface()
            else:
                self.BlinkSurface()
        elif self.configureGame == 5: # get all playernames and then create universe
            if keycode is not 13 and len(self.keyStrokesList) < 8: # return not pressed
                self.keyStrokesList.append(chr(keycode))
            else:
                if self.playerCount < self.numPlayers:
                    self.playerNames.append(''.join(self.keyStrokesList))
                    # self.playerWorlds.append(self.worldList[self.playerCount - 1]) # might not need if we can just call worldList when needed
                    self.keyStrokesList = []
                    self.playerCount += 1
                    self.AddText(''.join([self.playerNameText[0], str(self.playerCount), self.playerNameText[1], self.worldList[self.playerCount - 1], self.playerNameText[2]]), 0)
                    self.AddText(self.playerNameText[3], 1)
                    self.BlitTextSurface()
                elif self.playerCount == self.numPlayers:
                    self.playerNames.append(''.join(self.keyStrokesList))
                    # self.playerWorlds.append(self.worldList[self.playerCount - 1]) # might not need if we can just call worldList when needed
                    self.keyStrokesList= []
                    self.configureGame = 6
                    self.AddText(self.universeCreateText, 0)
                    self.BlitTextSurface()
                    self.imageViewer.Update()
                    time.sleep((0.2 * self.numWorlds))
                    self.CreateUniverse()
        elif self.configureGame == 6: # show universe, ask for new setup
            if keycode == 121 or keycode == 89 or keycode == 110 or keycode == 78: # y Y n N
                if keycode == 121 or keycode == 89:
                    self.AddText(self.universeReCreateText, 0)
                    self.BlitTextSurface()
                    self.imageViewer.Update()
                    time.sleep((0.2 * self.numWorlds))
                    self.CreateUniverse()
                else:
                    self.configureGame = 7
                    self.AddText(self.gameSetupText, 0)
                    self.BlitTextSurface()
                    self.imageViewer.Update()
                    time.sleep((0.2 * self.numWorlds) + (0.2 * self.numPlayers) + (0.2 * self.numTurns))
                    print "display new text for playing the game"
            print self.playerNames
        elif self.configureGame == 7: # start gameplay functionality for game
            print self.universeMap
            print self.worldLocations
            # need to first take into account which turn i'm in.  possibly run that in a rungame function
            # once run game is called, it sets a new bind function for the imageviewer for keypress which will allow me to start something
            # for capturing other than the current capturekeys function which is pretty long.
            
            # then i need to break down functions for each turn:
            # In 1 turn, the following happens:
            # 1. for each player,  input the ships to move from 1 world to another world.
            # 2. store this information to use when i get to a future turn where it becomes relevant.
            # 3. prior to any turns, when setup the game, I need to figure out a formula to determine how many turns it will take to 
            #    before the results of a move occur
            # 4. after a person inputs a turn, store the information of the turn as well as what turn this action occurs.
            # 5. i will need to store all this turn information in a variable so i can use it as need be.
            # 6. NEED TO STORE ACTUAL WORLDS AND THEIR COORDINATE POSITION IN A VARIABLE I CAN USE TO CALCULATE TURN INFORMATION
            # HAVE SELF.NUMWORLDS TO GIVE LENGTH OF USEFUL WORLDS TO STORE COORDINATES FOR
            # HAVE SELF.WORLDLIST TO STORE WHICH WORLD GOES WHERE, AS IN A,B,C,D,E
            # ONCE I HAVE THE COORD FOR EACH RELEVANT WORLD STORED, I CAN USE THAT TO CALCULATE HOW LONG IT WILL TAKE.
            # THEN I NEED TO LEARN TO STORE EACH TURN INFORMATION TO I CAN KEEP UP WITH WORLD NUMBER COUNTS
            
            print "start game now"
        event.Skip()

    def AddText(self, currentText, currentLine, top=0):
        self.tmpSize = self.mainDraw.textsize(currentText, font=self.gameFont)
        self.tmpWidth = self.GetSizeTuple()[0]/2 - self.tmpSize[0]/2
        if top == 0: self.tmpHeight = self.GetSizeTuple()[1]/2 - self.tmpSize[1]/2 - 50 + (25 * currentLine)
        else: self.tmpHeight = 10 + (25 * currentLine)
        if currentLine == 0: self.mainDraw.rectangle((0, 0, self.GetSizeTuple()[0], self.GetSizeTuple()[1]), fill="black", outline=None)
        self.mainDraw.text((self.tmpWidth, self.tmpHeight), currentText, font=self.gameFont, fill=171)

    def AddTitleText(self, currentText):
        self.tmpSize = self.mainDraw.textsize(currentText, font=self.titleFont)
        self.tmpWidth = self.GetSizeTuple()[0]/2 - self.tmpSize[0]/2
        self.tmpHeight = self.GetSizeTuple()[1]/2 - self.tmpSize[1]/2 - 50
        self.mainDraw.rectangle((0, 0, self.GetSizeTuple()[0], self.GetSizeTuple()[1]), fill="black", outline=None)
        self.mainDraw.text((self.tmpWidth, self.tmpHeight), currentText, font=self.titleFont, fill=171)
        
    def BlitTextSurface(self):
        self.ShowBitmapFromPIL()
        self.imageViewer.SetFocus()

    def ShowBitmapFromPIL(self): # when we operate on the image...
        self.wxImg = wx.EmptyImage(self.mainImage.size[0], self.mainImage.size[1])
        self.wxImg.SetData(self.mainImage.convert("RGB").tostring())
        self.wxImg.SetAlphaData(self.mainImage.convert("RGBA").tostring()[3::4])
        self.bmpImg = self.wxImg.ConvertToBitmap()
        self.mainBmp.SetBitmap(self.bmpImg)

    def BlinkSurface(self):
        self.mainBmp.Hide()
        self.imageViewer.Update()
        time.sleep(0.1)
        self.mainBmp.Show()
        self.imageViewer.Update()
        
    def CreateUniverse(self):
        self.universeMap = []
        print "create universe algorithm here.  should be a multi matrix of [20x20]"
        for i in range(20):
            self.universeMap.append([":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":", " ", ":"])
        # general empty map is created. now to populate with the number of worlds.
        for i in range(self.numWorlds):
            tmpCheck = 0
            print i
            while tmpCheck == 0:
                tmpCoord = self.GetRandomCoordinate()
                print tmpCoord
                if self.universeMap[tmpCoord[0]][tmpCoord[1]] is not ":" or self.universeMap[tmpCoord[0]][tmpCoord[1]] is not " ":
                    self.universeMap[tmpCoord[0]][tmpCoord[1]] = self.worldList[i]
                    self.worldLocations[self.worldList[i]] = tmpCoord
                    tmpCheck = 1
        # display universe on screen
        self.DisplayUniverse()
        # prompt for new setup
        self.AddText(self.askNewSetupText, len(self.universeMap) + 1, 1)
        # push all text to screen
        self.BlitTextSurface()                
        
    def GetRandomCoordinate(self):
        tmpCoord = [random.randint(0,19), random.randint(0,38)]
        return tmpCoord
    
    def InputTurn(self, tmpPlayer, tmpWorld):
        pass
    def DisplayUniverse(self):
        # display universe on the screen
        self.AddText(self.universeTitle, 0, 1)
        for index, row in enumerate(self.universeMap):
            self.AddText(''.join(row), index + 1, 1)
            self.BlitTextSurface()
            self.imageViewer.Update()
            time.sleep(0.5)
            self.imageViewer.Update()
    def CalculateTimeDistance(self, fromTmpWorld, toTmpWorld):
        # determine distance between two planets
        print self.worldLocations
        # now i have the world and its position.  I can simply take the difference in values to determine the number of turns to get to a world.