import turtle
alexa=turtle.Turtle()
alexa.screen.bgcolor("black")
alexa.speed(0)
colors=["red","green","white","orange","violet","purple","yellow"]
alexa.penup()
alexa.backward(400)
alexa.pendown()
for i in range(10):
    alexa.color(colors[i%len(colors)])
    alexa.circle(100)
    alexa.penup()
    alexa.forward(100)
    alexa.pendown()



turtle.done()
