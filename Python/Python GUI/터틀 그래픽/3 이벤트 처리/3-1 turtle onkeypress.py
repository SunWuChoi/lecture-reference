import turtle as t


def moveForward():
    t.forward(10)


def turnLeft():
    t.left(90)


def turnRight():
    t.right(90)


def turnBack():
    t.right(180)


t.shape("turtle")

# onkeypress( 함수, "키" )    # 지정한 키보드의 자판을 눌렀을 때
t.onkeypress(moveForward, "Up")
t.onkeypress(turnLeft, "Left")
t.onkeypress(turnRight, "Right")
t.onkeypress(turnBack, "Down")

# onkeyrelease( 함수, "키" )    # 지정한 키보드의 자판을 눌렀다가 뗐을 때

# listen()   # 키 입력 포커스를 줌
t.listen()

t.done()

