def print_asterisks (rows):
    for row in range (1, rows + 1):
       print("* " * row)
        # line = ""
        # for column in range (1, row + 1):
        #     line += "* "
        # print(line)

number = int(input("Enter number of rows of asterisks: "))
print_asterisks (number)