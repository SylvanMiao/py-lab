if __name__=="__main__":
    import turtle
    import time

    t=turtle.Pen()
    t.color('green','blue')
    t.hideturtle()

    t.begin_fill()
    for x in range(3):
        t.forward(180)
        t.left(180-60)
    t.forward(10)
    t.right(90)
    t.end_fill()

    t.color('green','brown')
    t.begin_fill()
    for x in range(3):
        t.forward(160)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(30,-160)
    t.color('green','teal')
    t.pendown()
    t.begin_fill()
    for x in range(3):
        t.right(90)
        t.forward(40)
    t.end_fill()

    t.penup()
    t.color('green','red')
    t.begin_fill()
    t.goto(100,200)
    t.circle(20)
    t.end_fill()



    time.sleep(5)
    