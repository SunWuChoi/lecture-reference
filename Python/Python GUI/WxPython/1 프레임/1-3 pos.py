import wx

app = wx.App()
# pos=(모니터 x 좌표, 모니터 y 좌표) x 는 커질수록 오른쪽으로 이동, y 는 커질수록 아래쪽으로 이동
frame = wx.Frame(None, pos=(100, 0))

frame.Show(True)
app.MainLoop()
