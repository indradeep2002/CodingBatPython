def non_start(a, b):
  n1 = len(a)
  n2 = len(b)
  
  if(n1 < 1 and n2 >= 1):
    
    return a+b[1:]
    
  elif (n2 < 1 and n1 >= 1):
    
    return a[1:]+b
    
  else:
    
    return a[1:]+b[1:]
  

a , b = input("Enter the strings: ").split(" ")

print(non_start(a,b))
