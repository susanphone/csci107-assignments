import math

def is_prime(number):
    for test in range (2, int(math.sqrt(number))+ 1):
        if number % test == 0:
            return False        
    return True

for i in range (1, 51):
    print(i, is_prime(i))



