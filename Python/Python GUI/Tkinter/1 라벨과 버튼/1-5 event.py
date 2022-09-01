import tkinter.font
from tkinter import *

mainFrame = Tk()
mainFrame.geometry("400x200")

# 이름을 저장하는 라벨
nameLabel = Label(mainFrame, text="이름", font="Serif 20")
nameLabel.pack()


# 이름 라벨의 텍스트를 "홍길동" 으로 바꿔주는 함수
# hongButton 이 changeHong 함수를 사용하기 때문에 버튼보다 먼저 선언해줘야한다
def changeHong():
    nameLabel["text"] = "홍길동"


hongButton = Button(mainFrame, text="홍길동으로 변경", command=changeHong)
hongButton.pack()


# 이름 라벨의 텍스트를 "성춘향" 으로 바꿔주는 함수
def changeSeong():
    nameLabel["text"] = "성춘향"


seongButton = Button(mainFrame, text="성춘향으로 변경", command=changeSeong)
seongButton.pack()

# 글씨 변경
nameLabel["text"] = "텍스트 변경 연습"

# 글씨 색상 변경
nameLabel["foreground"] = "red"

# 라벨 배경 색상 변경
nameLabel["background"] = "cyan"

# 글씨체/글씨 크기 변경
nameLabel["font"] = tkinter.font.Font(family="맑은 고딕", size=20, slant="italic")

# 기본적인 색상 "white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"
# 가능한 색상이 궁금하면 아래 링크 참조
# https://www.tutorialspoint.com/python/tk_colors.htm


mainFrame.mainloop()
