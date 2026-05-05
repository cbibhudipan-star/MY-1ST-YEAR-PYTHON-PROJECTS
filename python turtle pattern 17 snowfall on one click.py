import turtle
alexa=turtle.Turtle()
alexa.screen.bgcolor("black")
alexa.speed(200)

alexa.pensize(2)


def flower(x,y):
    alexa.penup()
    alexa.goto(x,y)
    alexa.pendown()
    alexa.color("white")
    for i in range(20):
        alexa.forward(50)
        alexa.color("blue","cyan")
        alexa.begin_fill()
        alexa.circle(5)
        alexa.end_fill()
        alexa.backward(100)
        alexa.forward(50)
        alexa.left(40)
alexa.getscreen().onclick(flower)
turtle.done()
