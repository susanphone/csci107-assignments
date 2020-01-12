# def fibonacci(n):
#     if n == 0:       #base case 1
#         return 0
#     elif n == 1:     #base case 2
#         return 1
#     else:           #general case
#         return fibonacci(n-1) + fibonacci(n-2)

# for i in range (50, 70):
#     print(i, fibonacci(i))

#in a loop
def fibonacci2(n):
    two_back = 0
    one_back = 1
    for i in range (2, n + 1):
        answer = two_back + one_back
        two_back = one_back
        one_back = answer
    return answer