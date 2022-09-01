from tkinter import *

mainFrame = Tk()

mainFrame.geometry("400x300")

# 라벨을 만드는 방법
# 변수 이름 = Label( 프레임, text = "글씨", font = "글꼴" )
fruitLabel = Label(mainFrame, text="과일들", font="Serif 20")

# 라벨의 위치를 잡아 주는 코드
fruitLabel.pack()

mainFrame.mainloop()
