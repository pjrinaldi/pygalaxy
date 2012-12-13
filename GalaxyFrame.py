from wx import wx
from PIL import Image, ImageFont, ImageDraw
import time

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
        self.titleFont = ImageFont.truetype("./resources/C64_Pro_v1.0-STYLE.ttf", 48)
        self.gameFont = ImageFont.truetype("./resources/C64_Pro_v1.0-STYLE.ttf", 12)
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
        self.worldList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        self.configureGame = 0
        self.numPlayers = 0
        self.numWorlds = 0
        self.numTurns = 0
        self.neutralBuild = 0
        self.newSetup = 0
        self.playerCount = 1
        self.playerNames = []
        self.playerWorlds = []
        self.mainImage = Image.new('L', self.GetSize())
        self.mainDraw = ImageDraw.Draw(self.mainImage)
        self.AddTitleText(self.titleText)
        self.wxBmp = wx.EmptyBitmap(self.GetSize()[0], self.GetSize()[1])
        self.mainBmp = wx.StaticBitmap(self.imageViewer, -1, self.wxBmp, wx.Point(0, 0))
        self.BlitTextSurface()
                
        self.Show(True)
    def CaptureKeys(self, event):
        keycode = event.GetKeyCode()
        if self.configureGame == 0:
            self.keyStrokesList = []
            self.configureGame = 1
            self.AddText(self.numPlayerText, 0)
            self.BlitTextSurface()
        elif self.configureGame == 1:
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
        elif self.configureGame == 2:
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
        elif self.configureGame == 3:
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
        elif self.configureGame == 4:
            if keycode == 121 or keycode == 89 or keycode == 110 or keycode == 78: # y Y n N
                if keycode == 121 or keycode == 89:
                    self.neutralBuild = 1
                else:
                    self.neutralBuild= 0
                self.configureGame = 5
                self.AddText(''.join([self.playerNameText[0], str(i+1), self.playerNameText[1], self.worldList[i], self.playerNameText[2]]), 0)
                self.AddText(self.playerNameText[3], 1)
                self.BlitTextSurface()
                # the loop works, but i need to do the loop for each configuregame function and break out...
                '''
                for i in range(self.numPlayers): # (i+1) is each player to set their name and world.
                    self.AddText(''.join([self.playerNameText[0], str(i+1), self.playerNameText[1], self.worldList[i], self.playerNameText[2]]), 0)
                    self.AddText(self.playerNameText[3], 1)
                    self.BlitTextSurface()
                    # need a variable to allow me to capture name of person, iterator i am on, and then return to this spot and conitue my loop
                    break
                    if i == range(self.numPlayers):
                        self.configureGame = 5
                        print "name config is done."
                '''
            else:
                self.BlinkSurface()
        elif self.configureGame == 5:
            if keycode is not 13: # return not pressed
                print "record keystrokes to get the name"
                print "possibly also count keystrokes and stop when reach 8"
                
            print "record keystrokes here for name."
            print "store the name and world designator in the respective field"
            print "iterate playerCount variable ++"
            print "set configureGame back to 4"
            print "if playerCount <= numPlayers: do what i need and go back to 4"
            print "otherwise do what i need and goto 6 to move on to the universe creation"
        event.Skip()

    def AddText(self, currentText, currentLine):
        self.tmpSize = self.mainDraw.textsize(currentText, font=self.gameFont)
        self.tmpWidth = self.GetSizeTuple()[0]/2 - self.tmpSize[0]/2
        self.tmpHeight = self.GetSizeTuple()[1]/2 - self.tmpSize[1]/2 - 50 + (25 * currentLine)
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
        print "create universe algorithm here.  should be a multi matrix of [20x20]"
        