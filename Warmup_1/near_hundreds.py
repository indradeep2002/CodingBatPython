#################################
# Given an int n, return True if it is within 10 of 100 or 200. 
# Note: abs(num) computes the absolute value of a number.
#################################


def near_hundreds(n):
    if (n in range(90, 111)):
        return True
    elif (n in range(190 , 211)):
        return True
    else:
        return False

print(near_hundreds(90)) # expected = True
print(near_hundreds(93)) # expected = True
print(near_hundreds(193)) # expected = True
print(near_hundreds(186)) # expected = False
print(near_hundreds(85)) # expected = False