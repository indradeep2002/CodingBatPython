def last2(str):
  n = len(str)
  count = 0
  target_str = str[n - 2:]
  for i in range(0, n-2):
    if(str[i] + str[i + 1] == target_str):
      count += 1
    
  return count

print(last2("hixxhi"))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))