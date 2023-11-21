def has23(nums):
  if (2 in nums) or (3 in nums) or (2 and 3 in nums):
    return True
  return False

l = [int(i) for i in input('Enter the values: ').split(" ")]
print(has23(l))