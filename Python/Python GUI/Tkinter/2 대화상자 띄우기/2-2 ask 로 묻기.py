from tkinter import *
import tkinter.messagebox

# 선택창(예, 아니오 버튼) - tkinter.messagebox.askyesno(제목, 메세지, 옵션)
# 선택창(예, 아니오, 취소 버튼) - tkinter.messagebox.askyesnocancel(제목, 메세지, 옵션)
# 선택창(예, 취소 버튼) - tkinter.messagebox.askokcancel(제목, 메세지, 옵션)
# 경고창(다시시도, 취소 버튼) - tkinter.messagebox.askretrycancel(제목, 메세지, 옵션)
# 선택창(예, 아니오 버튼) - tkinter.messagebox.askquestion(제목, 메세지, 옵션)

mainFrame = Tk()

tkinter.messagebox.askyesno("askyesno", "메세지")  # 예, 아니오 버튼
tkinter.messagebox.askyesnocancel("askyesnocancel", "메세지")  # 예, 아니오, 취소 버튼
tkinter.messagebox.askokcancel("askokcancel", "메세지")  # OK, 취소 버튼
tkinter.messagebox.askretrycancel("askretrycancel", "메세지")  # 다시 시도, 취소 버튼
tkinter.messagebox.askquestion("askquestion", "메세지")  # 예, 아니오 버튼

mainFrame.mainloop()
