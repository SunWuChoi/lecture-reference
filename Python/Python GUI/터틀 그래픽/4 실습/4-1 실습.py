import turtle as t

t.shape("turtle")

# 터틀 그래픽을 이용해 한 변의 길이가 60인 정사각형을 그려주세요
# 정사각형의 선 색상은 파란 색이어야 합니다.
t.pencolor("blue")
t.begin_fill()
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.end_fill()

t.forward(120)

# 터틀 그래픽을 이용해 반지름의 길이가 30인 원을 그려주세요
# 원의 내부 색상은 초록색이어야 합니다.
t.fillcolor("green")
t.begin_fill()
t.circle(30)
t.end_fill()

t.done()
