from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

mainFrame = Tk()
mainFrame.geometry('400x300')

# 메인 화면에는 라벨 하나와 버튼 하나를 만들어주세요.
lbl1 = Label(mainFrame)

# 라벨에는 '로그인 프로그램' 이라는 글씨가 보이게 만들어주세요.
lbl1["text"] = "로그인 프로그램"


# 로그인을 하는 프로그램을 UI를 통해 구현해주세요.
# 버튼을 누르면 아이디와 비밀번호를 입력하는 대화 상자를 띄워주세요.
def login():
    inputID = tkinter.simpledialog.askstring("입력", "아이디를 입력하세요")
    inputPW = tkinter.simpledialog.askstring("입력", "비밀번호를 입력하세요")

    # 아이디가 '1' 이고 비밀번호가 'a' 라고 입력되면 '환영합니다' 라는 대화상자를, 아니면 '정보가 옳지 않습니다' 라는 대화상자를 띄워주세요.
    if inputID == "1" and inputPW == "a":
        tkinter.messagebox.showinfo("결과", "환영합니다!")
    else:
        tkinter.messagebox.showwarning("결과", "정보가 옳지 않습니다.")


# 메인 화면에는 라벨 하나와 버튼 하나를 만들어주세요.
btn1 = Button(mainFrame, text="로그인", command=login)

lbl1.pack()
btn1.pack()

mainFrame.mainloop()
