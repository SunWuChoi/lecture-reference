from tkinter import *

mainFrame = Tk()
mainFrame.geometry("500x500")

# pack 에 아무것도 안쓰고 실행시 먼저 선언한 버튼부터 위에서 아래로 순서대로 표시

b1 = Button(mainFrame, text="1")
b1.pack()

b2 = Button(mainFrame, text="2")
b2.pack()

b3 = Button(mainFrame, text="3")
b3.pack()

b4 = Button(mainFrame, text="4")
b4.pack()

mainFrame.mainloop()
