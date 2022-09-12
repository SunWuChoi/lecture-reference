import turtle as t

t.shape("turtle")

# 터틀 그래픽을 이용해 오각형, 육각형, 칠각형을 만들어주세요.
# 각 도형의 선 색상은 빨강, 파랑, 노랑입니다.
# 각 도형의 내부 색상은 원하는 색으로 세 도형이 모두 다르게 만들어주세요.

t.fillcolor("yellow")
t.begin_fill()
t.pencolor("red")
t.circle(60, 360, 5)
t.end_fill()

t.forward(130)
t.fillcolor("gray")
t.begin_fill()
t.pencolor("blue")
t.circle(60, 360, 6)
t.end_fill()

t.forward(130)
t.fillcolor("pink")
t.begin_fill()
t.pencolor("yellow")
t.circle(60, 360, 7)
t.end_fill()

t.done()
