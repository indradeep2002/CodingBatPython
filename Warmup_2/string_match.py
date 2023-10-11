def string_match(a, b):
  nA = len(a)
  nB = len(b)
  count = 0
  flag = False
  
 
  
  if nA > 0 and nB > 0:
    if (nB < nA):
       for i in range(nB - 1):
          tar_str = b[i] + b[i+1]
          if(a[i] + a[i+1] == tar_str):
            count += 1

  
    elif (nA < nB):
      for i in range(nA - 1):
        tar_str = a[i] + a[i+1]
        if(b[i] + b[i+1] == tar_str):
            count += 1
          
    else:
      for i in range(nA - 1):
        tar_str = a[i] + a[i+1]
        if(b[i] + b[i+1] == tar_str):
            count += 1
          

    return count 
      
  else:
    return count 
  
print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))