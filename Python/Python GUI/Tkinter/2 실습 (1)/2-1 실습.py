from tkinter import *

mainFrame = Tk()
mainFrame.geometry('400x300')

# 중앙에 "위치" 라는 글이 쓰여져있는 라벨을 하나 만들고 왼쪽과 오른쪽 벽에 붙어있게 버튼을 각각 하나씩 만들어주세요!
Label = Label(mainFrame, text="위치")
Label.pack()


# 중앙에 있는 라벨에 "왼쪽" 이라는 글씨가 뜨게
def setLeft():
    Label["text"] = "왼쪽"


# 중앙에 있는 라벨에 "오른쪽"이라는 글씨가 뜨게
def setRight():
    Label["text"] = "오른쪽"


# 왼쪽에 있는 버튼을 누르면 중앙에 있는 라벨에 "왼쪽" 이라는 글씨가 뜨게 만들어주세요.
leftButton = Button(mainFrame, command=setLeft)
leftButton.pack(side="left")

# 오른쪽에 있는 버튼을 누르면 중앙에 있는 라벨에 "오른쪽"이라는 글씨가 뜨게 만들어주세요.
RightButton = Button(mainFrame, command=setRight)
RightButton.pack(side="right")

mainFrame.mainloop()
