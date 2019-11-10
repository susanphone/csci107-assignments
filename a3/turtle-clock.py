#Draw a blue turtle in center
#Set backgriund color to light green
#Figure out how to draw one dash and turtle
#Figure out how to do all 12

import turtle
window = turtle.Screen()
window.bgcolor("blue violet")

clock = turtle.Turtle()
clock.shape("turtle")
clock.color("aqua")
clock.hideturtle()

clock.stamp()

for clock_hand in range (12):
    clock.penup()
    clock.forward(100)
    clock.pendown()
    clock.forward(20)
    clock.penup()
    clock.forward(30)
    clock.stamp()
    clock.goto(0, 0) 
    clock.right(360 / 12)

window.exitonclick()

#for number in range(10)  <------- list
# for year in range (1990, 2019, 2) :
#     print(year)