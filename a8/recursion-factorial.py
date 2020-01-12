def factorial(n):
    if n ==0:       #base case
        return 1
    else:           #general case (always involves recursion)
        return factorial (n-1) * n

for i in range (20):
    print (i, factorial(i))

def factorial2(n):
    answer = 1
    for i in range (2, n+1):
        answer *= i
    return answer

for i in range (20):
    print(i, factorial(i), factorial2(i))

# def recursion (n):
#     if n<= 100:
#         print(n)
#         recursion(n + 1)

# recursion(7)
# #M.C. Escher - self reference
# #Factorial