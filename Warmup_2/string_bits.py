def string_bits(str):
  new_str = ""
  
  for i in range(len(str)):
    if (i % 2 == 0):
      new_str += str[i]
  
  return new_str


print(string_bits("Hello"))
print(string_bits("Hi"))
print(string_bits('Heeololeo'))