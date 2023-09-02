#################################################
# Given a string, 
# return a new string where the first and last chars have been exchanged.
#
#################################################

def front_back(str):
  #return (str[len(str) - 1]+str[1:len(str)-1)] + str[0])
  if len(str) > 1:
    front = str[0]
    back = str[len(str) - 1]
    mid = str[1: len(str) -1]
    return (back + mid + front)
  else:
    return str

# Test Cases :
print(front_back('code') ) # -> 'eodc'
print(front_back('a') ) # -> 'a'
print(front_back('ab') ) # -> 'ba'