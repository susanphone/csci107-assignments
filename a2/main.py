first = input("Please enter first name > ")
last = input("Please enter last name > ")
number = input("Please enter telephone number ex. (xxx)-xxx-xxxx > ")
# first= "bill"
# last = "fold"
# number = "(011)-899-9881"

full_name = last + ", " + first
contact = number + "   @: " + first + "@parasail.com"


print("\nHere is your business card...\n")

print("+------------------------------------------------+")
print("|    |                                           |")
print("|   -|          " + full_name.ljust(33) +   "|")
print("|  --|          Tribute Liabilities Associate    |")
print("| ---|          Parasail Capital                 |")
print("| ---------                                      |")
print("|  -------      4 Hunger Plaza                   |")
print("|               STE 1400                         |")
print("|               District 12, Panem 00012         |")
print("|                                                |")
print("| Work:" + contact.ljust(42) + "|")
print("+------------------------------------------------+")
