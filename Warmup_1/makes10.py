###############################
# Given 2 ints, a and b, 
# return True if one if them is 10 or if their sum is 10.
#
###############################


def makes10(a , b):
    if ((a == 10) or (b == 10)):
        return True
    elif ((a + b) == 10):
        return True
    else:
        return False


print(makes10(9 , 10)) # expected = True
print(makes10(9 , 9)) # expected = False
print(makes10(1 , 9)) # expected = True