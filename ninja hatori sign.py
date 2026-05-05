import turtle
t=turtle.Turtle()
t.getscreen().bgcolor("black")
t.pencolor("blue")
for i in range(900):
    for j in range(4):
        t.forward(10+i)
        t.left(10)
t.done()
    
