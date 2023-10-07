def front_times(str, n):
  if (len(str) > 3):
    first = str[:3]
    return first * n
  else:
    return str * n


print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))