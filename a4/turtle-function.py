import turtle

def draw_polygon (polygon, sides, length) :
    for side in range(sides) :
        polygon.forward(length)
        polygon.left(360 - (360 / sides))   #<------ can draw any polygon

def create_turtle (turtle_color, x, y):
    generic_turtle=turtle.Turtle()
    generic_turtle.hideturtle()
    generic_turtle.up()
    generic_turtle.goto(x, y)
    generic_turtle.down()
    generic_turtle.color(turtle_color)
    return generic_turtle


window = turtle.Screen()

octagon = create_turtle("red", 100, 100)
draw_polygon (octagon, 8, 50)

square = create_turtle("blue", -250, -77)
draw_polygon (square, 4, 100)

window.exitonclick()
