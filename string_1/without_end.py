def without_end(str):
  n = len(str)
  
  if (n < 2):
    return ""
  
  return str[1:n-1]

user_input = input("Enter the string: ")

print(without_end(user_input))