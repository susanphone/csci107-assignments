import turtle
window = turtle.Screen()
window.bgcolor("grey")


def draw_brick(brick, bottom_left_x, bottom_left_y, side_length, brick_color):
    brick.penup()
    brick.goto(bottom_left_x, bottom_left_y)
    brick.pendown()
    brick.pencolor("magenta")
    brick.fillcolor(brick_color)
    brick.begin_fill()
    for side in range(4):
        brick.forward(side_length)
        brick.left(90)
    brick.end_fill()


def draw_body(brick, start_x, start_y, length, color_to_use, rows, columns):
    y = start_y
    for row in range(rows):
        x = start_x
        for column in range(columns):
            draw_brick(brick, x, y, length, color_to_use)
            x = x + length
        y = y + length

square = turtle.Turtle()
square.hideturtle()
square.speed(0)
square.fillcolor("magenta")
square.color("magenta")

side_length = 20
bricks_per_row = 9
draw_body(square, -side_length * bricks_per_row / 2, 0, side_length, "purple", 9, bricks_per_row)

window.exitonclick()
