from tkinter import *

mainFrame = Tk()

mainFrame.geometry("400x300")

# 버튼을 만드는 방법
# 변수 이름 = Button( 프레임, text="버튼에 쓰여질 글", foreground="버튼 색상" )
appleButton = Button(mainFrame, text="사과", foreground="Red")

# 버튼의 위치를 잡아 주는 코드
appleButton.pack()

mainFrame.mainloop()
