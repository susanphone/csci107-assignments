name= input("Enter your name: ")
width = int(input("Enter the field width: "))

dashes = ""
for i in range(width - 4):
    dashes = dashes + "-"

banner = "+ " + dashes + " +"
name_line = "|" + name.center(width - 2) + "|"

print (banner)
print (name_line)
print (banner)





# a = float(input("Enter a: "))
# b = float(input(" Enter b: "))
# x = -b / a
# print("The equation ax + b = 0 when x =", x)






# import turtle
# window = turtle.Screen()

# legs = input("Enter number of legs: ")
# legs = int(legs)

# sprite = turtle.Turtle()
# sprite.hideturtle()
# sprite.color("green")

# for leg in range(legs):
#     sprite.forward(20)
#     sprite.backward(20)
#     sprite.left(360 / legs)

# window.exitonclick()






# number = input("Enter an integer from 1 to 9: ")
# number = int(number)

# for i in range(1, number + 1):
#     print(str(i).rjust(i))


