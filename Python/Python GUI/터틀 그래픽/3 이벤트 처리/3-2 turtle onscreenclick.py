import turtle as t


def colorRed():
    t.pencolor("red")


def colorBlue():
    t.pencolor("blue")


def colorGreen():
    t.pencolor("green")


def width1():
    t.pensize(1)


def width3():
    t.pensize(3)


def width5():
    t.pensize(5)


def moveForward(x, y):
    t.setpos(x, y)


def checkpoint():
    t.stamp()
    t.ontimer(checkpoint, 5000)


def clearAll():
    t.clear()


t.shape("turtle")

t.onkeypress(colorRed, "r")
t.onkeypress(colorBlue, "b")
t.onkeypress(colorGreen, "g")

t.onkeypress(width1, "1")
t.onkeypress(width3, "3")
t.onkeypress(width5, "5")

t.onkeypress(clearAll, "Down")

# onscreenclick( 함수, 버튼 )    # 마우스로 프로그램 화면을 클릭했을 때
t.onscreenclick(moveForward)

# ontimer( 함수, 시간 )    # 일정 시간 이후에 어떤 함수를 작동시킬 때
t.ontimer(checkpoint, 5000)

t.listen()
t.done()
