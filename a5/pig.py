import turtle
window = turtle.Screen()
window.bgcolor("grey")

square = turtle.Turtle()
square.fillcolor("magenta")
square.color("magenta")

#need to create a function to repeat squares.
#Try creating a movable x coordinate. Then y.
for sides in range (4):
    square.begin_fill()
    square.forward(20)
    square.right(90)
square.end_fill()

square.goto(20, 0)
for sides in range(4):
        square.begin_fill()
        square.forward(20)
        square.right(90)

square.goto(40,0)
for sides in range (4):
        square.begin_fill()
        square.forward(20)
        square.right(90)

square.goto(60,0)
for sides in range(4):
        square.begin_fill()
        square.forward(20)
        square.right(90)

window.exitonclick()
