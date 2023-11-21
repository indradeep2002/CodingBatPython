def max_end3(nums):
  if nums[0] < nums[2]:
    
    nums[0] = nums[2]
    nums[1] = nums[2]
    return nums
  
  elif nums[0] > nums[2]:
    
    nums[1] = nums[0]
    nums[2] = nums[0]
    
    return nums
    
  else:
    
    nums[0] = nums[2]
    nums[1] = nums[2]
    
    return nums

l = l = [int(i) for i in input('Enter the values: ').split(" ")]
print(max_end3(l))