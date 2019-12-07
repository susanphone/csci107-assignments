import turtle
import random

window = turtle.Screen()
line = turtle.Turtle()

width = window.window_width()
height = window.window_height()

def draw_line(drawing_turtle, x, y, distance):
    drawing_turtle.penup()
    drawing_turtle.goto(x, y)
    drawing_turtle.pendown()
    drawing_turtle.forward(distance)

x = -width/6
y = height/2
line.right(90)

line.pencolor(random.random(), random.random(), random.random()) #------> (r, g, b)
draw_line(line, x, y, height)
line.pencolor(random.random(), random.random(), random.random())
draw_line(line, -x, y, height)

height = window.window_height()

# def draw_line(drawing_turtle, x, y, distance):
#     drawing_turtle.penup()
#     drawing_turtle.goto(-880, y)
#     drawing_turtle.pendown()
#     drawing_turtle.forward(distance)
    

x = width/5
y = height/2
line.left(90)
height = 405
height = height - 162
height = height - 162


line.pencolor(random.random(), random.random(),random.random())
draw_line(line, -880, 243, width)

line.penup()
line.goto(-880, 81)
line.pendown()
line.pencolor(random.random(), random.random(), random.random())
draw_line(line, -880, 81, width)

line.penup()
line.goto(-880, -81)
line.pendown()
line.pencolor(random.random(), random.random(), random.random())
draw_line(line, -880, -81, width)

line.penup()
line.goto(-880, -243)
line.pendown()
line.pencolor(random.random(), random.random(), random.random())
draw_line(line, -880, -243, width)

window.exitonclick()
