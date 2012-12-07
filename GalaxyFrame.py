from wx import wx

class GalaxyFrame(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.SetBackgroundColour(wx.Colour(0, 0, 0))
        
        self.Show(True)