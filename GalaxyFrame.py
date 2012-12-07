from wx import wx
import Image, ImageFont, ImageDraw

class GalaxyFrame(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.imageViewer = wx.Panel(self, style=wx.BORDER_NONE)
        self.imageViewer.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.imageViewer.Bind(wx.EVT_CHAR, self.CaptureKeys)
        self.mainBitmap = None
        self.mainBox = wx.BoxSizer(wx.VERTICAL)
        self.mainBox.Add(self.imageViewer, 1, wx.ALL | wx.EXPAND | wx.ALIGN_LEFT)
        self.SetSizer(self.mainBox)
        self.TitleFont = ImageFont.truetype("./resources/C64_Pro_v1.0-STYLE.ttf", 48)
        self.gameFont = ImageFont.truetype("./resources/C64_Pro_v1.0-STYLE.ttf", 12)
        
        self.configureGame = 0
        self.numPlayers = 0
        
        self.DisplayText(self.imageViewer, "PYTHON GALAXY!", self.TitleFont, 0, None)

        self.Show(True)

    def CaptureKeys(self, event):
        keycode = event.GetKeyCode()
        if self.configureGame == 0:
            self.configureGame = 1
            self.DisplayText(self.imageViewer, "HOW MANY PLAYERS (1-20)?", self.gameFont, 0, None)
        elif self.configureGame == 1:
            self.configureGame = 2
            self.DisplayText(self.imageViewer, "HOW MANY WORLDS (5-40)?", self.gameFont, 1, self.mainBitmap.GetBitmap())
        print keycode
        event.Skip()
        
    def DisplayText(self, currentPanel, currentText, currentFont, currentLines, currentBitmap):
        if currentBitmap == None:
            self.tmpText = Image.new('L', self.GetSize())
        else:
            self.tmpImg = wx.ImageFromBitmap(currentBitmap)
            self.tmpText = Image.new('RGB', (self.tmpImg.GetWidth(), self.tmpImg.GetHeight()))
            self.tmpText.fromstring(self.tmpImg.GetData())
        self.tmpDraw = ImageDraw.Draw(self.tmpText)
        self.tmpSize = self.tmpDraw.textsize(currentText, font=currentFont)
        self.tmpWidth = self.GetSizeTuple()[0]/2 - self.tmpSize[0]/2
        self.tmpHeight = self.GetSizeTuple()[1]/2 - self.tmpSize[1]/2 - 50 + (25 * currentLines)
        self.tmpDraw.text((self.tmpWidth, self.tmpHeight), currentText, font=currentFont, fill=235)
        self.mainBitmap = self.ShowBitmapFromPIL(currentPanel, self.tmpText)
        currentPanel.SetFocus()
        

    def ShowBitmapFromPIL(self, currentPanel, currentPIL): # when we operate on the image...
        self.wxImg = wx.EmptyImage(currentPIL.size[0], currentPIL.size[1])
        self.wxImg.SetData(currentPIL.convert("RGB").tostring())
        self.wxImg.SetAlphaData(currentPIL.convert("RGBA").tostring()[3::4])
        self.bmpImg = self.wxImg.ConvertToBitmap()
        currentPanel.DestroyChildren()
        self.bmp = wx.StaticBitmap(currentPanel, -1, self.bmpImg, wx.Point(0,0), wx.Size(currentPIL.size[0], currentPIL.size[1]))
        return self.bmp
