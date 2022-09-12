import turtle as t

t.shape("turtle")

# 터틀 그래픽을 통해 위 그림에 나와있는 도형을 그려주세요.

# 노란 별 그리기
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()

# 하늘색 채운 네모 그리기
t.pencolor("black")
t.right(180)
t.penup()
t.forward(20)
t.pendown()
t.fillcolor("skyblue")
t.begin_fill()

for i in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

t.penup()
t.right(180)
t.forward(10)
t.pendown()

# 네모 바깥에 검은 테두리 그리기
t.left(90)
t.forward(110)
t.left(90)
for i in range(3):
    t.forward(120)
    t.left(90)
t.forward(10)

# 깃발 그릴곳으로 이동후 깃발의 왼쪽 아래에서 오른쪽 보기
t.penup()
t.forward(200)
t.right(90)
t.pensize(10)

# 무지개 깃발 그리기
rainbow = ["red", "orange", "yellow", "green", "skyblue", "blue", "purple"]
isCheck = 1

t.pendown()
for i in rainbow:
    t.pencolor(i)
    t.forward(100);
    t.penup()
    # 이번에 짝수줄 그렸으면 다음 홀수줄을 위해 위로 올라가서 오른쪽보기
    if isCheck % 2 == 0:
        t.right(90)
        t.forward(10)
        t.right(90)
    # 이번에 홀수줄 그렸으면 다음 짝수줄을 위해 위로 올라가서 왼쪽보기
    else:
        t.left(90)
        t.forward(10)
        t.left(90)
    t.pendown()
    isCheck += 1
t.penup()

t.forward(250)

t.done()
