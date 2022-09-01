from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

mainFrame = Tk()
mainFrame.geometry('400x300')

# 화면에 라벨 두 개와 버튼 하나를 만들어주세요.
label1 = Label(mainFrame)
label2 = Label(mainFrame)

# 첫 번째 라벨에는 "예"라는 글씨를, 두 번째 라벨에는 "아니오"라는 글씨가 나오게 해주세요.
label1["text"] = "예"
label2["text"] = "아니오"


# 버튼을 눌렀을 때, 나오는 대화상자에서 예를 누르면 첫 번째 라벨의 배경 색상이 파란 색으로 변하게 만들어주세요.
# 버튼을 눌렀을 때, 나오는 대화상자에서 아니오를 누르면 두 번째 라벨의 배경 색상이 빨간 색으로 변하게 만들어주세요.
def onClick():
    choice = tkinter.messagebox.askyesno("질문", "선택해주세요")
    if choice:
        label1["background"] = "blue"
    else:
        label2["background"] = "red"


# 버튼을 눌렀을 때, 나오는 대화상자에서 예를 누르면 첫 번째 라벨의 배경 색상이 파란 색으로 변하게 만들어주세요.
button1 = Button(mainFrame, text="버튼", command=onClick)

label1.pack()
label2.pack()
button1.pack()

mainFrame.mainloop()
