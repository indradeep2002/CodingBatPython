def same_first_last(nums):
  n = len(nums)
  
  if n >= 1 and nums[0] == nums[n-1]:
    return True
  else:
    return False


lis = [int(i) for i in input('Enter the values: ').split(' ')]

print(same_first_last(lis))