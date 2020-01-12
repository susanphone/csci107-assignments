def starts_with_red (string):
    if string == "":
        return False
    else:
        return (string[0] == "r") 
    if string[0] == "r":
        return True
    else:
        return False
def four_or_more_reds (string):
    count = 0
    for ch in string:
        if ch == "r":
            count += 1

    return (count >= 4)
    # if count >= 4:
    #     return True
    # else:
    #     return False
def alternating_colors (string):
    last_character = ""

    for current_character in string:
        if current_character == last_character:
            return False
        last_character = current_character
    return True

def manufactoria():

    # test(starts_with_red, "rbbrb")
    # test(starts_with_red, "rrrr")
    # test(starts_with_red, "br")
    # test(starts_with_red, "")

    print("Testing four or more  reds")
    print("------------------------------")
    # test(four_or_more_reds, "")
    # test(four_or_more_reds, "r")
    # test(four_or_more_reds, "b")
    # test(four_or_more_reds, "rbbbbbrbbbbbrbbbb")
    # test(four_or_more_reds, "bbbbrbbbb")
    # test(four_or_more_reds, "rrrrr")
    # test(four_or_more_reds, "brrbrr")



# for ch in "csci 107":
#     print(ch)
