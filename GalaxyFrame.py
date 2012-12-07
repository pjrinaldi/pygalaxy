from wx import wx
import Image, ImageFont, ImageDraw
import time

class GalaxyFrame(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.imageViewer = wx.Panel(self, style=wx.BORDER_NONE)
        self.imageViewer.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.imageViewer.Bind(wx.EVT_CHAR, self.CaptureKeys)
        self.mainBox = wx.BoxSizer(wx.VERTICAL)
        self.mainBox.Add(self.imageViewer, 1, wx.ALL | wx.EXPAND | wx.ALIGN_LEFT)
        self.SetSizer(self.mainBox)
        self.TitleFont = ImageFont.truetype("./resources/C64_Pro_v1.0-STYLE.ttf", 48)
        self.gameFont = ImageFont.truetype("./resources/C64_Pro_v1.0-STYLE.ttf", 12)
        self.keyStrokesList = []
        
        self.TitleText = "PYTHON GALAXY!"
        self.numPlayerText = "HOW MANY PLAYERS (1-20)?"
        self.numWorldsText = "HOW MANY WORLDS (5-40)?"
        self.configureGame = 0
        self.numPlayers = 0
        self.numWorlds = 0
        
        self.mainImage = Image.new('L', self.GetSize())
        self.mainDraw = ImageDraw.Draw(self.mainImage)
        self.AddText(self.TitleText, self.TitleFont, self.mainDraw, 0)
        self.BlitTextSurface(self.imageViewer, self.mainImage)
                
        self.Show(True)

    def CaptureKeys(self, event):
        keycode = event.GetKeyCode()
        if self.configureGame == 0:
            self.keyStrokesList = []
            self.configureGame = 1
            self.mainImage = Image.new('L', self.GetSize())
            self.mainDraw = ImageDraw.Draw(self.mainImage)
            self.AddText(self.numPlayerText, self.gameFont, self.mainDraw, 0)
            self.BlitTextSurface(self.imageViewer, self.mainImage)
        elif self.configureGame == 1:
            if keycode > 47 and keycode < 58:
                self.keyStrokesList.append(keycode - 48)
            elif keycode == 13:
                testNum = ""
                print self.keyStrokesList
                for i in self.keyStrokesList:
                    testNum = testNum + str(i)
                print testNum
                print "Need to validate number and redisplay if not valid, otherwise continue on"
                if int(testNum) > 0 and int(testNum) < 21:                    
                    self.configureGame = 2
                    self.mainImage = Image.new('L', self.GetSize())
                    self.mainDraw = ImageDraw.Draw(self.mainImage)
                    self.numPlayerText = self.numPlayerText + " " + testNum
                    self.AddText(self.numPlayerText, self.gameFont, self.mainDraw, 0)
                    self.AddText(self.numWorldsText, self.gameFont, self.mainDraw, 1)
                    self.BlitTextSurface(self.imageViewer, self.mainImage)
                else:
                    self.configureGame = 1
                    self.keyStrokesList = []
                    self.imageViewer.Hide()
                    # self.bmp.Hide()
                    time.sleep(1)
                    # self.bmp.Show()
                    self.imageViewer.SetBackgroundColour(wx.Colour(0, 0, 0))
                    self.mainImage = Image.new('L', self.GetSize())
                    self.mainDraw = ImageDraw.Draw(self.mainImage)
                    self.AddText(self.numPlayerText, self.gameFont, self.mainDraw, 0)
                    self.BlitTextSurface(self.imageViewer, self.mainImage)
        print keycode
        event.Skip()

    def DisplayText(self, currentPanel, currentText, currentFont):
        self.tmpText = Image.new('L', self.GetSize())
        self.tmpDraw = ImageDraw.Draw(self.tmpText)
        self.tmpSize = self.tmpDraw.textsize(currentText, font=currentFont)
        self.tmpWidth = self.GetSizeTuple()[0]/2 - self.tmpSize[0]/2
        self.tmpHeight = self.GetSizeTuple()[1]/2 - self.tmpSize[1]/2 - 50
        self.tmpDraw.text((self.tmpWidth, self.tmpHeight), currentText, font=currentFont, fill=215)
        self.ShowBitmapFromPIL(currentPanel, self.tmpText)
        currentPanel.SetFocus()

    def AddText(self, currentText, currentFont, currentDraw, currentLine):
        print "Add Text to pil surface"
        self.tmpSize = currentDraw.textsize(currentText, font=currentFont)
        self.tmpWidth = self.GetSizeTuple()[0]/2 - self.tmpSize[0]/2
        self.tmpHeight = self.GetSizeTuple()[1]/2 - self.tmpSize[1]/2 - 50 + (25 * currentLine)
        currentDraw.text((self.tmpWidth, self.tmpHeight), currentText, font=currentFont, fill=215)

    def BlitTextSurface(self, currentPanel, currentPIL):
        print "display text surface to screen"
        self.ShowBitmapFromPIL(currentPanel, currentPIL)
        currentPanel.SetFocus()

    def ShowBitmapFromPIL(self, currentPanel, currentPIL): # when we operate on the image...
        self.wxImg = wx.EmptyImage(currentPIL.size[0], currentPIL.size[1])
        self.wxImg.SetData(currentPIL.convert("RGB").tostring())
        self.wxImg.SetAlphaData(currentPIL.convert("RGBA").tostring()[3::4])
        self.bmpImg = self.wxImg.ConvertToBitmap()
        currentPanel.DestroyChildren()
        if self.bmp: self.bmp.Destroy()
        self.bmp = wx.StaticBitmap(currentPanel, -1, self.bmpImg, wx.Point(0,0), wx.Size(currentPIL.size[0], currentPIL.size[1]))