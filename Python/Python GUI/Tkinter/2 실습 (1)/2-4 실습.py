from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

mainFrame = Tk()
mainFrame.geometry('400x300')

# 화면에 라벨 두 개와 버튼 하나를 만들어주세요.
label1 = Label(mainFrame)
label2 = Label(mainFrame)

# 첫 번째 라벨에는 "이름"이라는 글씨가, 두 번째 라벨에는 "나이"라는 글씨가 뜨게 해주세요.
label1["text"] = "이름"
label2["text"] = "나이"


# 버튼을 누르면 이름을 입력할 수 있는 대화 상자랑 나이를 입력할 수 있는 대화상자가 차례대로 나오게 해주세요.
def inputBox():
    name = tkinter.simpledialog.askstring("질문", "이름을 입력하세요")

    # 이 때, 나이를 입력하는 대화상자에 문자를 입력하면 에러가 나와야 합니다.
    age = tkinter.simpledialog.askinteger("질문", "나이를 입력하세요")  # askinteger -> 숫자 이외 입력시 에러

    # 이 대화 상자에 이름과 나이를 입력하고 확인을 누르면 첫 번째 라벨에는 이름이, 두 번째 라벨에는 나이가 출력되게 만들어주세요.
    label1["text"] = name
    label2["text"] = age


# 화면에 라벨 두 개와 버튼 하나를 만들어주세요.
# 버튼을 누르면 이름을 입력할 수 있는 대화 상자랑 나이를 입력할 수 있는 대화상자가 차례대로 나오게 해주세요.
button1 = Button(mainFrame, text="클릭", command=inputBox)

label1.pack()
label2.pack()
button1.pack()

mainFrame.mainloop()
