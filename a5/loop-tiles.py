import turtle
import math
window = turtle.Screen()

def draw_brick(brick, bottom_left_x, bottom_left_y, side_length,brick_color) :
    brick.penup()
    brick.goto(bottom_left_x, bottom_left_y)
    brick.pendown()
    brick.pencolor("black")
    brick.fillcolor(brick_color)
    brick.begin_fill()
    for side in range (4):
        brick.forward(side_length)
        brick.left(90)
    brick.end_fill()

def draw_body(brick, start_x, start_y, length, color_to_use, rows, columns) :
    y = start_y
    for row in range (rows):
        x = start_x
        for column in range (columns):
            draw_brick (brick, x, y, length, color_to_use)
            x = x + length
        y = y + length


def draw_pyramid(brick, start_x, start_y, length, color_to_use, columns):
    y = start_y
    x = start_x
    bricks_in_row = columns
    rows = math.ceil(columns / 2)
    for row in range(1, rows + 1):
        for column in range(bricks_in_row):
            draw_brick(brick, x, y, length, color_to_use)
            x = x + length
        y = y + length
        x = start_x + (length * row)
        bricks_in_row -= 2

drawing = turtle.Turtle()
drawing.hideturtle()
drawing.speed(0)

side_length = 20
bricks_per_row = 19

# draw_body(drawing, -side_length * bricks_per_row / 2, 0, side_length, "purple", 5, bricks_per_row)
draw_pyramid(drawing, -side_length * bricks_per_row / 2,0, side_length, "purple", bricks_per_row)

window.exitonclick()
