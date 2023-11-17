def common_end(a, b):
  nA = len(a)
  nB = len(b)
  

  if nA > nB and (a[0] == b[0]) or (a[nA - 1] == b[nB - 1]):
    return True
    
  elif nB > nA and (b[0] == a[0]) or (b[nB - 1] == a[nA - 1]):
    return True
  
  elif nB == nA and a[0] == b[0] or a[nA - 1] == b[nB - 1]:
    return True
    
  else:
    return False


lisa = [int(i) for i in input('Enter the values for a : ').split(' ')]

lisb = [int(i) for i in input('Enter the values for b : ').split(' ')]

print(common_end(lisa, lisb))