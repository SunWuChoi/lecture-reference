import turtle as t

t.shape("turtle")


# 터틀 그래픽을 이용해 간단한 그림판을 만들어주세요.
# 만든 그림판은 아래의 조건을 만족해야 합니다.

def drawing():
    t.forward(10)


def eraseAll(x, y):
    t.clear()


def turnLeft():
    t.left(90)


def turnRight():
    t.right(90)


def changeRed():
    t.pencolor("red")


def changeBlack():
    t.pencolor("black")


def changeGreen():
    t.pencolor("green")


def drawCircle():
    t.circle(10)


# 1. 10 초마다 현재 위치를 stamp()를 통해 표시해야 합니다
def timerOn():
    t.stamp()
    t.ontimer(timerOn, 10000)


# 10 초마다 스탬프 찍는 함수 시작
timerOn()

# 3. 방향키를 통해 거북이가 움직이며 그림을 그려야 합니다.
t.onkeypress(drawing, "Up")
t.onkeypress(turnLeft, "Left")
t.onkeypress(turnRight, "Right")

# 4. 키보드 자판을 통해 선의 색상을 바꿀 수 있어야 합니다.
t.onkeypress(changeRed, "r")
t.onkeypress(changeBlack, "b")
t.onkeypress(changeGreen, "g")

# 5. C 자판을 누르면 반지름이 10 인 원을 그려야 합니다.
t.onkeypress(drawCircle, "c")

# 2. 마우스 좌클릭을 하면 화면에 그려진 그림이 모두 지워져야 합니다.
t.onscreenclick(eraseAll, "1")

t.listen()

t.done()
