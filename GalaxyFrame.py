from wx import wx
import Image, ImageFont, ImageDraw

class GalaxyFrame(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.imageViewer = wx.Panel(self, style=wx.BORDER_NONE)
        self.imageViewer.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.mainBox = wx.BoxSizer(wx.VERTICAL)
        self.mainBox.Add(self.imageViewer, 1, wx.ALL | wx.EXPAND | wx.ALIGN_LEFT)
        self.SetSizer(self.mainBox)
        self.gameFont = ImageFont.truetype("./resources/C64_Pro_v1.0-STYLE.ttf", 12)
        
        # self.DisplayText(self.imageViewer, "DO YOU WANT TO RETURN TO AN OLD GAME (O) OR START A NEW(N) ONE?", self.gameFont)
        
        self.Show(True)
        
    def DisplayText(self, currentPanel, currentText, currentFont):
        self.tmpText = Image.new('L', self.GetSize())
        self.tmpDraw = ImageDraw.Draw(self.tmpText)
        self.tmpSize = self.tmpDraw.textsize(currentText, font=currentFont)
        self.tmpWidth = self.GetSizeTuple()[0]/2 - self.tmpSize[0]/2
        self.tmpHeight = self.GetSizeTuple()[1]/2 - self.tmpSize[1]/2 - 50
        self.tmpDraw.text((self.tmpWidth, self.tmpHeight), currentText, font=currentFont, fill=235)
        self.ShowBitmapFromPIL(currentPanel, self.tmpText)
        

    def ShowBitmapFromPIL(self, currentPanel, currentPIL): # when we operate on the image...
        self.wxImg = wx.EmptyImage(currentPIL.size[0], currentPIL.size[1])
        self.wxImg.SetData(currentPIL.convert("RGB").tostring())
        self.wxImg.SetAlphaData(currentPIL.convert("RGBA").tostring()[3::4])
        self.bmpImg = self.wxImg.ConvertToBitmap()
        currentPanel.DestroyChildren()
        self.bmp = wx.StaticBitmap(currentPanel, -1, self.bmpImg, wx.Point(0,0), wx.Size(currentPIL.size[0], currentPIL.size[1]))
