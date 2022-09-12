import turtle as t

# t.shape("turtle")   # 거북이
# t.shape("classic")  # 클래식
# t.shape("triangle") # 삼각형
# t.shape("arrow")    # 화살촉
# t.shape("square")   # 사각형
# t.shape("circle")   # 원

# t.forward( 픽셀 )
# t.backward( 픽셀 )
# t.left( 각도 )
# t.right( 각도 )

t.shape("turtle")

t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

# 끝나도 창을 끄지 않고 기다리는 함수
t.done()

