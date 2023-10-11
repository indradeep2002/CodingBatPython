def array_front9(nums):
  n = len(nums)
  
  if(n <= 3):
    for i in range(0,n):
      if(nums[i] == 9):
        return True
    return False
 
  if(n >= 4):
    for i in range(0,4):
      if(nums[i] == 9):
        return True
  
    return False


print(array_front9([1 , 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1 , 2, 3, 4, 5]))