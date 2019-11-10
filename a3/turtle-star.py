#draw a star using turtle graphics.

import turtle
window = turtle.Screen()

points = 7
angle= 180 - (180 / points)
star = turtle.Turtle()
star.speed(10)
star.hideturtle()
star.backward(50)
#star.goto(-50, 0)

for i in range(points):
    star.forward(100)
    star.right(angle)

window.exitonclick()


