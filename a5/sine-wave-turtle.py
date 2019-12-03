import turtle
import math
window = turtle.Screen()
window.setworldcoordinates(-1, -1.1, 11, 1.1)

graph = turtle.Turtle()
graph.hideturtle()
graph.speed(0)

x = 0.0
for i in range (1000):
    graph.goto(x, math.sin(x))
    x += 0.01

window.exitonclick()