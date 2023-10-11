def array123(nums):
  n = len(nums)
  
  if(n < 3):
    return False
  
  for i in range(0, n - 2):
    if (nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3):
      return True
    
  return False

print(array123([1 , 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))