from tkinter import *

mainFrame = Tk()
mainFrame.geometry('400x300')

# 화면 중앙에 라벨 2개와 버튼 2개를 만들어주세요.
label1 = Label(mainFrame)
label2 = Label(mainFrame)

# 첫 번째 라벨에는 "크기" 라는 글씨가
label1["text"] = "크기"

# 두 번째 라벨에는 "색상"이라는 글씨가 나타나게 만들어주세요.
label2["text"] = "색상"


# 첫 번째 라벨 속 글자 크기가 변하는 함수
def textSize():
    label1["font"] = "Arial 40"


# 두 번째 라벨 속 글자 색상을 파란색으로 바꾸는 하는 함수
def textColor():
    label2["foreground"] = "blue"


# 첫 번째 버튼을 누르면 첫 번째 라벨 속 글씨 크기가 변하도록 만들어주세요. (한 번만 변해도 됩니다)
button1 = Button(mainFrame, text="크기", command=textSize)

# 두 번째 버튼을 누르면 두 번째 라벨 속  글자 색상이 파란색으로 변하도록 만들어주세요. (한 번만 변해도 됩니다.)
button2 = Button(mainFrame, text="색상", command=textColor)

label1.pack()
label2.pack()
button1.pack()
button2.pack()

mainFrame.mainloop()
