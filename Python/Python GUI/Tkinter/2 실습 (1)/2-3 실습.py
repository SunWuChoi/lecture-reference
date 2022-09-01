from tkinter import *
import tkinter.messagebox

mainFrame = Tk()
mainFrame.geometry('400x300')

# 화면에 라벨과 버튼을 하나 만들어주세요.
label1 = Label(mainFrame)

# 라벨에는 "정보 보여주기" 라는 글씨가 써있게 해주세요.
label1["text"] = "정보 보여주기"


# 정보라는 제목의 창을 띄우고 코딩온 20 이라는 정보 메세지를 띄우는창
def showInfo():
    tkinter.messagebox.showinfo("정보", "코딩온 20")


# 화면에 라벨과 버튼을 하나 만들어주세요.
# 버튼을 누르면 알림창을 통해 자신의 이름과 나이가 보여주게 만들어주세요.
button1 = Button(mainFrame, text="버튼", command=showInfo)

label1.pack()
button1.pack()

mainFrame.mainloop()
