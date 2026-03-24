import turtle
if __name__=="__main__":
    turtle.penup()
    turtle.color('green','red')
    turtle.goto(100,100)
    turtle.pendown()

    turtle.goto(100,-100)
    turtle.goto(-100,-100)
    turtle.goto(-100,100)
    turtle.goto(100,100)
    turtle.goto(5,215)
    turtle.goto(-108,90)
    turtle.speed(speed=10)

    turtle.done()