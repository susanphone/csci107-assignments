#Minecraft Pig: Each tile is 20 x 20 , use the turtkle to draw the tile
# the x and y coordinates of the upper left corner of the tile, and the color in use.
import turtle
window = turtle.Screen()
window.bgcolor("gray")

def create_tile(tile_color):
    new_tile = turtle.Turtle()
    new_tile.hideturtle()
    new_tile.color(tile_color)
    return new_tile

pig_skin = create_tile("pink")


def coordinates(tile_in_row, tile_in_column):
    upper_left_x = - (20 + tile_in_row)
    upper_left_y = 20 + tile_in_column
    for square in range(4):
        pig_skin.forward(20)
        pig_skin.right(90)
        pig_skin.up()
        pig_skin.goto(upper_left_x, upper_left_y)
        pig_skin.down()


window.exitonclick()
