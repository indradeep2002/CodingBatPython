def first_last6(nums):
  n = len(nums)
  
  
  if len(nums) < 1:
    return False
    
  if len(nums) == 1 and nums[0] == 6:
    return True
  
  elif nums[0] == 6 or nums[n-1] == 6:
    return True
  
  else:
    return False
  

lis = [int(i) for i in input('Enter the values: ').split(' ')]
#print(lis)
print(first_last6(lis))