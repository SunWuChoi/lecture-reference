import wx

app = wx.App()
# size=(가로 길이, 세로 길이)
frame = wx.Frame(None, size=(200, 100))

frame.Show(True)
app.MainLoop()
