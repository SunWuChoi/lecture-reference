from tkinter import *

# 메인 프레임 선언, 앞으로 이걸 수정 하면서 창을 만든다
mainFrame = Tk()

# 아래 코드로 제목을 수정
# title = 제목
mainFrame.title("파이썬 그래픽 테스트")

# 아래 코드로 창 크기를 수정
# geometry("가로 x 세로")
# geometry = 기하학, 모양
mainFrame.geometry("400x200")

# 아래 코드로 창 크기 조절 안되게 고정
mainFrame.resizable(False, False)

# .mainloop() 을 실행 하면 창을 실행
mainFrame.mainloop()

# 참고하기 좋은 사이트
# https://076923.github.io/posts/#Tkinter