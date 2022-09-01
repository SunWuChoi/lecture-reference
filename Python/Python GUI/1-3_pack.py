from tkinter import *

mainFrame = Tk()
mainFrame.geometry("500x500")

# 버튼을 선언 하고 pack 을 이용해 위치를 지정

b1 = Button(mainFrame, text="1")
b1.pack(side="left")

b2 = Button(mainFrame, text="2")
b2.pack(side="right")

b3 = Button(mainFrame, text="3")
b3.pack(side="top")

b4 = Button(mainFrame, text="4")
b4.pack(side="bottom")

mainFrame.mainloop()
