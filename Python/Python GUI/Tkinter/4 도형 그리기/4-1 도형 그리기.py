from tkinter import *

mainFrame = Tk()
sketchbook = Canvas(mainFrame, width=400, height=200)
sketchbook.pack()

# 선 그리기
# sketchbook.create_line(시작지점x좌표, 시작지점y좌표, 도착지점x좌표, 도착지점y좌표, fill="선색상")
sketchbook.create_line(10, 10, 100, 100, fill="red")

# 사각형 그리기
# sketchbook.create_rectangle(좌측상단x좌표, 좌측상단y좌표, 우측하단x좌표, 우측하단y좌표, outline="선색상", width="선 굵기", fill="채우기색상")
sketchbook.create_rectangle(110, 10, 200, 100, outline="black", width="3")

# 원 그리기
# sketchbook.create_oval(좌측상단x좌표, 좌측상단y좌표, 우측하단x좌표, 우측하단y좌표, outline="선색상", width="선 굵기", fill="채우기색상")
sketchbook.create_oval(210, 10, 300, 100, fill="yellow")

mainFrame.mainloop()
