def left2(str):
  
  n = len(str)
  
  if (n <= 2):
    return str
    
  return str[2:]+str[:2]


user_input = input("Enter the string: ")

print(left2(user_input))