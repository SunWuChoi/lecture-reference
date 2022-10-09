import wx

app = wx.App()
frame = wx.Frame(None)


def onClick(event):
    print("Clicked")


btn = wx.Button(frame, label="클릭")
btn.Bind(wx.EVT_BUTTON, onClick)

frame.Show()
app.MainLoop()