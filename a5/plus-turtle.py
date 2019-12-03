import turtle
length = int(input("Enter a number between 50 and 500: "))
window = turtle.Screen()
window.bgcolor("gold")
plus = turtle.Turtle()
plus.pensize(20)
plus.color("blue")
#1
"""plus.forward(length / 2)
plus.backward(length)
plus.forward(length / 2)
plus.right(90)
plus.forward(length / 2)
plus.backward(length)"""
#2
for segment in range (4):
    plus.forward(length / 2)
    plus.goto(0,0)
    plus.left(90)


window.exitonclick()
