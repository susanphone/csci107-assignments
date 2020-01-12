name = "President Cruzado"

def change_name():
    name = input("please enter a new name: ")
    return name

print (name)
name = change_name()
print (name)

#method 2: use of global

def change_name():
    global name
    name = input("please enter a new name: ")

print(name)
change_name()
print(name)
