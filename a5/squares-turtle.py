import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
def create_turtle(turtle_color, turtle_speed, turtle_pensize):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.color(turtle_color)
    new_turtle.speed(turtle_speed)
    new_turtle.pensize(turtle_pensize)
    return new_turtle

q7 = create_turtle("hotpink", 0, 1)

def draw_square(square, length): 
    upper_left_x = - (length / 2)
    upper_left_y = length / 2
    square.up()
    square.goto(upper_left_x, upper_left_y)
    square.down()
    for side in range(4):
        square.forward(length)
        square.right(90)
def main():
    length = 0
    how_many = int(input("How many squares? "))
    turtle_color = input("What color? ")
    increment = int(input("What is the increment of the squares? "))
    q7.color(turtle_color)
    for square in range(how_many):
            draw_square(q7, length)
            length = length + increment
main()
# draw_square(square, 20)
# draw_square(square, 40) 
# draw_square(square, 60)
# draw_square(square, 80)
# draw_square(square, 100)

window.exitonclick()
