name = "champ"
type(name)
name + " the bobcat"
name * 4

name[0]
name[1]
name[-1]

for index in range(len(name)):
    print(index)

for index in range(len(name)):
    print(name[index])

name.upper()
name.lower()
name.capitalize()
sentence= " Four score   and seven  "
sentence.strip()
sentence.lstrip()
sentence.rstrip()
sentence.count("o")
sentence.replace("o", "z")
while sentence.count(" ") > 0:
    sentence = sentence.replace("  ", " ")

sentence.center(25)
sentence.ljust(25)
sentence.rjust(25)

print("{} is my name".format("Susan"))

price = 2.33
print("The cost is ${}".format(price))
print("The cost is ${:5}".format(price))
print("Thje cost is ${:1}".format(price))
price = 10/3
print("The cost is ${:2f}".format(price)) #Digits to the right of the decimal

sentence[:5]
sentence[3:]
sentence[3:8]

