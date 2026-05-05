import turtle
alexa=turtle.Turtle()
alexa.screen.bgcolor("black")
alexa.speed(200)

alexa.pensize(2)


def flower(x,y):
    alexa.penup()
    alexa.goto(x,y)
    alexa.pendown()
    alexa.color("yellow")
    for i in range(20):
        alexa.circle(100,60)
        alexa.left(120)
        alexa.circle(20,60)
        alexa.left(20)
alexa.getscreen().onclick(flower)
turtle.done()
