import turtle
t = turtle.Turtle()
t.speed(0)
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
angle = 0
size = 1
while 1:
    for i in range(5):
        t.forward(150)
        t.left(72)
    t.right(1)
    angle += size
    if angle >= 120 / size:
        break
turtle.done()
