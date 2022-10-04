import wx

app = wx.App()
# name 은 이름, id 는 추후 이벤트 연결시 사용
frame = wx.Frame(None, name="frameName", id=wx.ID_ANY)

frame.Show(True)
app.MainLoop()
