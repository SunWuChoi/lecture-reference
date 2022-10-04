import wx

app = wx.App()
frame = wx.Frame(None)


def onButtonClick(event):
    print("x좌표 : ", event.x)
    print("y좌표 : ", event.y)


# Bind 을 이용해서 이벤트(여기선 마우스 왼쪽 클릭) 와 함수를 연결 할수있다
frame.Bind(wx.EVT_LEFT_DOWN, onButtonClick)


def onKeyClick(event):
    print("누른 자판 : ", chr(event.KeyCode))


# Bind 을 이용해서 이벤트(여기선 마우스 왼쪽 클릭) 와 함수를 연결 할수있다
frame.Bind(wx.EVT_CHAR, onKeyClick)

frame.Show(True)
app.MainLoop()

# event.x   : 현재 마우스가 눌린 위치의 x좌표
# event.y   : 현재 마우스가 눌린 위치의 좌표
# event.KeyCode : 현재 눌린 자판의 아스키코드

