from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

mainFrame = Tk()
mainFrame.geometry('400x300')

lbl1 = Label(mainFrame)
lbl1["text"] = "로그인 프로그램"


def login():
    inputID = tkinter.simpledialog.askstring("입력", "아이디를 입력하세요")
    inputPW = tkinter.simpledialog.askstring("입력", "비밀번호를 입력하세요")
    if inputID == "1" and inputPW == "a":
        tkinter.messagebox.showinfo("결과", "환영합니다!")
    else:
        tkinter.messagebox.showwarning("결과", "정보가 옳지 않습니다.")


btn1 = Button(mainFrame, text="로그인", command=login)

# 메인 프레임에 메뉴바를 붙여주세요.
menu1 = Menu(mainFrame)
mainFrame.config(menu=menu1)

shapeMenu = Menu(menu1)
helpMenu = Menu(menu1)

# 해당 메뉴에는 '도형' 이라는 메뉴와 '도움말' 이라는 메뉴가 있어야 합니다.
menu1.add_cascade(label="도형", menu=shapeMenu)
menu1.add_cascade(label="도움말", menu=helpMenu)

# '도형' 메뉴에는 '원', '사각형', '선'이라는 메뉴 항목이 있어야 합니다.
shapeMenu.add_command(label="원")
shapeMenu.add_command(label="사각형")
shapeMenu.add_command(label="선")

# '도움말' 메뉴에는 '정보', '확인' 이라는 메뉴 항목이 있어야 합니다.
helpMenu.add_command(label="정보")
helpMenu.add_command(label="확인")

lbl1.pack()
btn1.pack()

mainFrame.mainloop()
