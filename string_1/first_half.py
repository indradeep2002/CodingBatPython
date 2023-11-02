def first_half(str):
  n = len(str) // 2
  
  return str[:n]


user_input = input("Enter the String: ")

print(first_half(user_input))