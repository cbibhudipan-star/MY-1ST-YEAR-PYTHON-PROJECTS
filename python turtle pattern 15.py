import turtle
alexa=turtle.Turtle()
alexa.screen.bgcolor("black")
alexa.speed(200)



colors=["#ED3915","#FAD905","#05FA0D","#05FAD5","#0532FA","#C505FA","#FA055B","#FA0519"]
for i in range(900):
    alexa.color(colors[i%len(colors)])
    alexa.forward(i+250)
    for i in range(20):
        alexa.left(10)
        alexa.forward(20)
        alexa.backward(20)
        alexa.forward(10)
    alexa.penup()
    alexa.goto(0,0)
    alexa.pendown()
    alexa.left(i+5)
turtle.done()
