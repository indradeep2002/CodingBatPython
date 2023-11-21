def sum2(nums):
  if len(nums) <= 0:
    return 0
    
  elif len(nums) < 2:
    return sum(nums)
    
  else:
    return nums[0] + nums[1]


l = [int(i) for i in input('Enter the values: ').split(" ")]
print(sum2(l))