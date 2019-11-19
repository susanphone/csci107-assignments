import turtle
window = turtle.Screen()
window.bgcolor("gray")

star= turtle.Turtle()
points = int(input("Enter points for clock face: "))
angle = (180 - (180 / points))
star.speed(0)
star.color("purple")
star.pensize(3)
star.goto(-150, 0)
star.hideturtle()
star.backward(200)
for i in range(points):
    star.forward(800)
    star.right(angle)

clock = turtle.Turtle()
clock.shape("turtle")
clock.color("aqua")
clock.hideturtle()
clock.penup()
clock.goto(50, 0)
clock.pendown()
clock.stamp()
clock.pensize(5)

for clock_hand in range(12):
    clock.penup()
    clock.forward(100)
    clock.pendown()
    clock.forward(40)
    clock.penup()
    clock.forward(60)
    clock.stamp()
    clock.goto(50, 0)
    clock.right(360 / 12)

window.exitonclick()
