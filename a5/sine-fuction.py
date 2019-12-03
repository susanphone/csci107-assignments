def sum_to(n): 
    answer = 0
    for number in range (1, n + 1):
        answer = answer + number
    return answer
#this is a fruitful function ---^

#option 2!
def sum_to_2(n): 
    return n * ((n + 1) / 2)
