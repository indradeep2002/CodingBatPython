def combo_string(a, b):
  n1 = len(a)
  n2 = len(b)
  
  if (n1 > n2):
    return b+a+b
  
  elif (n2 > n1):
    return a + b + a
    
  else:
    return a+b+a
  
a , b = input("Enter the strings: ").split(" ")

print(combo_string(a, b))