def rotate_left3(nums):
  
  return [nums[1], nums[2], nums[0]]


lis = [int(i) for i in input('Enter the values: ').split(' ')]
print(rotate_left3(lis))