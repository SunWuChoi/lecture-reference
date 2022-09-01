from tkinter import *
import tkinter.messagebox

# 알림창(확인 버튼 1 개) - tkinter.messagebox.showinfo(제목, 메세지, 옵션)
# 경고창(확인 버튼 1 개) - tkinter.messagebox.showwarning(제목, 메세지, 옵션)
# 에러창(확인 버튼 1 개) - tkinter.messagebox.showerror(제목, 메세지, 옵션)

mainFrame = Tk()

tkinter.messagebox.showinfo("정보 보여주기", "showinfo 대화상자")
tkinter.messagebox.showwarning("경고 보여주기", "showwarning 대화상자")
tkinter.messagebox.showerror("에러 보여주기", "showerror 대화상자")

mainFrame.mainloop()
