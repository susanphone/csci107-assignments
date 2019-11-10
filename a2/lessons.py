#Math conversions for money and temperature. 

string_pennies = input ("Enter number of pennies: ")
penny = int(string_pennies)

nickel = penny // 5
#penny = penny - nickel * 5
penny = penny % 5
#Get pennies from user and calculate nickels and pennies. Then print nickel and pennies.

print("Nickels", nickel)
print("Pennies", penny)


string_celsius= input("Enter Celcius Temperature: ")
celsius = float(string_celsius)
#float(input("Enter Celsius temperature: "))
fahrenheit = celsius * (9 / 5) + 32

print("Farenheit temperature:", fahrenheit)

#Shows how to move things left and right or center them.
color1 = "greeeee4"
color2 = "|"
print(color1.ljust(5) + color2)