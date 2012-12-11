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
        self.playerNameText1 = "FLEET ADMIRAL 1 WILL BEGIN THE GAME IN CONTROL OF WORLD:(A)"
        self.playerNameText2 = "WHAT NAME WILL THIS FLEET ADMIRAL USE (1 TO 8 CHARACTERS)?"
        self.universeCreateText = "PLEASE WAIT WHILE I CREATE THE UNIVERSE"
        self.askNewSetupText = "NEW SETUP?"
        self.universeReCreateText = "PLEASE WAIT WHILE I REARRANGE THE STARS"
        self.gameSetupText = "NOW WAIT WHILE I SETUP THE GAME"
        self.configureGame = 0
        self.numPlayers = 0
        self.numWorlds = 0
        self.numTurns = 0
        self.neutralBuild = 0
        self.newSetup = 0
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
        event.Skip()

    def AddText(self, currentText, currentLine):
        self.tmpSize = self.mainDraw.textsize(currentText, font=self.gameFont)
        self.tmpWidth = self.GetSizeTuple()[0]/2 - self.tmpSize[0]/2
        self.tmpHeight = self.GetSizeTuple()[1]/2 - self.tmpSize[1]/2 - 50 + (25 * currentLine)
        if currentLine == 0: self.mainDraw.rectangle((0, 0, self.GetSizeTuple()[0], self.GetSizeTuple()[1]), fill="black", outline=None)
        self.mainDraw.text((self.tmpWidth, self.tmpHeight), currentText, font=self.gameFont, fill=215)

    def AddTitleText(self, currentText):
        self.tmpSize = self.mainDraw.textsize(currentText, font=self.titleFont)
        self.tmpWidth = self.GetSizeTuple()[0]/2 - self.tmpSize[0]/2
        self.tmpHeight = self.GetSizeTuple()[1]/2 - self.tmpSize[1]/2 - 50
        self.mainDraw.rectangle((0, 0, self.GetSizeTuple()[0], self.GetSizeTuple()[1]), fill="black", outline=None)
        self.mainDraw.text((self.tmpWidth, self.tmpHeight), currentText, font=self.titleFont, fill=215)
        
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
        print "start sleep"
        time.sleep(0.1)
        print "end sleep"
        self.mainBmp.Show()
        self.imageViewer.Update()
        
    def CreateUniverse(self):
        print "create universe algorithm here.  should be a multi matrix of [20x20]"
        