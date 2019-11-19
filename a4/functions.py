import math
def area_of_circle (radius): 
    answer = math.pi * (radius ** 2)
    return answer             #<--------Would be none without this function

radius = float(input("Enter radius "))
print("The area of a circle with the radius", radius, "= ", area_of_circle(radius))
