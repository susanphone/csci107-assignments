def is_it_a_leap_year (year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return True
    elif (year % 4) == 0:
        return True
    else: 
        return False


print (2000, is_it_a_leap_year(2000))
print (2004, is_it_a_leap_year(2004))
print (2018, is_it_a_leap_year(2018))
print (2019, is_it_a_leap_year (2019))
