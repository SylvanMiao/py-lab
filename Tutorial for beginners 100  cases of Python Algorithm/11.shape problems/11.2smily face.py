if __name__=="__main__":
    import turtle
    #face
    turtle.width(2)
    turtle.color("black")
    turtle.circle(120)

    #eyes
    turtle.penup()
    turtle.goto(-60,130)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(20)

    turtle.penup()
    turtle.goto(60,130)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(20)

    #mouth
    turtle.penup()
    turtle.goto(-60,45)
    turtle.color("pink")
    turtle.pendown()
    
    turtle.setheading(90)
    len=1
    for j in range(60):
        if j>30:
            len+=0.2
        else:
            len-=0.2
        turtle.forward(len)
        turtle.left(3)
    turtle.goto(-60,45)
    turtle.done()