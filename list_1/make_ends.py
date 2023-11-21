def make_ends(nums):
  n = len(nums)
  
  if n <= 0:
    return []
    
  elif n == 1:
    return [nums[0], nums[n-1]]
    
  else:
    return [nums[0] , nums[n-1]]

l = [int(i) for i in input('Enter the values: ').split(" ")]

print(make_ends(l))