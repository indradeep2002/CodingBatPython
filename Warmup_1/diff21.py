#########################
# Given an int n, return the absolute difference between n and 21, 
# except return double the absolute difference if n is over 21.
#########################


def diff21(n):
    if n < 21:
        return abs(n - 21)
    else:
        return (2 * (abs(n - 21)))




print(diff21(19)) # expected = 2
print(diff21(10)) # expected = 11
print(diff21(32)) # expected = 22
print(diff21(21)) # expected = 0