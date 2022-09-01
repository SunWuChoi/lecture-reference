from tkinter import *
import tkinter.simpledialog

# 정수를 입력 받음 - tkinter.simpledialog.askinteger("제목", "메세지")
# 입력 받은 것을 문자열로 취급 - tkinter.simpledialog.askstring("제목", "메세지")

mainFrame = Tk()

name = tkinter.simpledialog.askstring("제목", "이름을 입력하세요")
print(name)

age = tkinter.simpledialog.askinteger("제목", "나이를 입력하세요")
print(age)

mainFrame.mainloop()
