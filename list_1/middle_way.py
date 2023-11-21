def middle_way(a, b):
  return [a[1], b[1]]


l1 = [int(i) for i in input('Enter the values: ').split(" ")]
l2 = [int(i) for i in input('Enter the values: ').split(" ")]

print(middle_way(l1, l2))