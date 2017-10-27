from turtle import Turtle, Screen

playGround = Screen()
playGround.screensize(500, 500)
playGround.title("Turtle Keys")


run = Turtle("turtle")
run.speed(10)
run.color("peach puff")
run.penup()
run.setposition(-250, 250)
run.shapesize(2)
run.pendown()
run.pensize(4)

follow = Turtle("turtle")
follow.speed(8)
follow.color("purple")
follow.penup()
follow.setposition(-250, -250)
follow.shapesize(4)
def k1():
    run.forward(10)

def k2():
    run.left(10)

def k3():
    run.right(10)

def k4():
    run.backward(10)

def quitThis():
    playGround.bye()

def noMark():
    run.penup()

def clear():
    run.clear()

def Mark():
    run.pendown()
    
def follow_runner():
    follow.setheading(follow.towards(run))
    follow.forward(1)
    playGround.ontimer(follow_runner, 10)

playGround.onkey(k1, "Up")  # the up arrow key
playGround.onkey(k2, "Left")  # the left arrow key
playGround.onkey(k3, "Right")  # you get it!
playGround.onkey(k4, "Down")
playGround.onkey(quitThis, 'q')
playGround.onkey(noMark, 'n')
playGround.onkey(Mark, 'm')
playGround.onkey(clear, "c")
playGround.listen()

follow_runner()

playGround.mainloop()


