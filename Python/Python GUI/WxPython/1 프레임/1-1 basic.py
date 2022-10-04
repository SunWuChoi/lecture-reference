import wx

# App() 은 wx 모듈 사용하기 위해 선언
app = wx.App()
# Frame() 은 프레임을 만들어주는 함수, 부모 프레임은 속성이 없기 때문에 None
frame = wx.Frame(None)

# Show() 는 보여줄지 말지 True False 로 결정
frame.Show(True)
app.MainLoop()

# Frame(None) 여기서 None 에 넣을수 있는 것들

# parent : 상위 프레임을 쓰는 부분, 최상위 프레임의 경우 None을 써준다.
# id     : 프레임에 아이디를 지정하는 부분, 다른 프레임과 구별하기 위해 사용하는 속성 ( 우리가 임의로 값을 지정할 수 없음 )
# title  : tkinter에서의 title과 동일, 해당 프레임의 메인바에 나타날 이름을 정하는 속성
# pos    : 프레임이 화면에 처음 나타날 위치를 지정하는 속성
# size   : 프레임의 사이즈를 지정하는 속성
# style  : 프레임의 스타일 속성을 지정하는 부분, 자세한 부분은 뒤에 설명
# name   : 프레임의 이름을 지정하는 부분, id와 비슷한 용도로 사용한다.
