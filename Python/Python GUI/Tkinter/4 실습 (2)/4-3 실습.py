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

menu1 = Menu(mainFrame)
mainFrame.config(menu=menu1)

shapeMenu = Menu(menu1)
helpMenu = Menu(menu1)

menu1.add_cascade(label="도형", menu=shapeMenu)
menu1.add_cascade(label="도움말", menu=helpMenu)


# 도형 메뉴의 '원'을 누르면 화면에 원이 그려지게 만들어주세요.
# 원 도형은 다른 도형보다 선이 굵어야 하며 안에는 분홍색으로 채워져 있어야 합니다.
def drawCircle():
    cv.create_oval(30, 30, 50, 50, width=2, fill="pink")


# 도형 메뉴의 '사각형'을 누르면 화면에 사각형이 그려지게 만들어주세요.
# 사각형 도형의 선 색상은 초록색이어야 합니다.
def drawRect():
    cv.create_rectangle(30, 100, 20, 20, outline="green")


# 도형 메뉴의 '선'을 누르면 화면에 선이 그려지게 만들어주세요.
# 선 도형의 선 색상은 보라색이어야 합니다.
def drawLine():
    cv.create_line(170, 30, 150, 10, fill="purple")


# 도형 메뉴의 '원'을 누르면 화면에 원이 그려지게 만들어주세요.
shapeMenu.add_command(label="원", command=drawCircle)

# 도형 메뉴의 '사각형'을 누르면 화면에 사각형이 그려지게 만들어주세요.
shapeMenu.add_command(label="사각형", command=drawRect)

# 도형 메뉴의 '선'을 누르면 화면에 선이 그려지게 만들어주세요.
shapeMenu.add_command(label="선", command=drawLine)

helpMenu.add_command(label="정보")
helpMenu.add_command(label="확인")

cv = Canvas(mainFrame, width=200, height=100)

cv.pack()
lbl1.pack()
btn1.pack()

mainFrame.mainloop()
