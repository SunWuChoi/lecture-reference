import wx

app = wx.App()
frame = wx.Frame(None)

lbl = wx.StaticText(frame, label="라벨에 입력된 텍스트")

frame.Show()
app.MainLoop()