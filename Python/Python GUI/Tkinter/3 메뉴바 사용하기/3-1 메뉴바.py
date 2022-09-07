from tkinter import *

mainFrame = Tk()
mainFrame.geometry("400x200")

# 메뉴바 선언, Menu(메뉴 넣을 프레임)
menubar = Menu(mainFrame)

# mainFrame 에 메뉴바 연결
mainFrame.config(menu=menubar)

# 메뉴에 넣을 아이템 선언
item = Menu(menubar)

# 메뉴에 "파일" 이라는 이름의 메뉴 아이템 추가
menubar.add_cascade(label="파일", menu=item)


# 파일 메뉴에서 저장누르면 실행되는 함수
def save():
    print("저장 버튼")


def delete():
    print("삭제 버튼")


# 파일 메뉴에 기능 추가 ( 이름만 저장 혹은 삭제고 실제로는 save(), delete() 함수 발동 )
item.add_command(label="저장", command=save)
item.add_command(label="삭제", command=delete)

mainFrame.mainloop()
