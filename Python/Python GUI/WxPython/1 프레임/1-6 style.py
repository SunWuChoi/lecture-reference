import wx

app = wx.App()
frame = wx.Frame(None, style=wx.MAXIMIZE | wx.CAPTION | wx.CLOSE_BOX)

# style= 에 사용할수 있는 것들

# ICONIZE # 최소화 상태로 프레임을 띄운다.
# STAY_ON_TOP # 다른 창들보다 항상 위에 존재한다.
# MAXMIZE # 최대화 상태로 프레임을 띄운다.
# FRAME_NO_TASKBAR # 작업 표시줄에 나타나지 않게 한다.
# CAPTION # 시스템 바를 표시한다.
# CLOSE_BOX # 닫기 버튼을 만든다.
# MAXIMIZE_BOX # 최대화 버튼을 만든다.

frame.Show(True)
app.MainLoop()
