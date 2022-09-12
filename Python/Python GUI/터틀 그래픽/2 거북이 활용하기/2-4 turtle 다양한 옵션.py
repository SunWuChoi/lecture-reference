import turtle as t

t.shape("turtle")

# bgcolor( 색상 )    # 배경 색상을 칠하는 코드
t.bgcolor("green")

# fillcolor( 색상 )     # 도형 내부 색상을 지정하는 코드
t.fillcolor("yellow")

# begin_fill()    # 내부 색상을 칠하는 코드
t.begin_fill()

t.circle(40)
t.forward(100)
t.circle(40)

# end_fill()     # 내부 색상 칠하기를 끝내는 코드
t.end_fill()

t.forward(100)
t.circle(40)

t.done()