

def string_splosion(str):
  final_str = ""
  sub_str = ""
  
  for i in range(len(str)):
    sub_str = sub_str +  str[i]
    final_str = final_str +  sub_str
    
  return final_str


print(string_splosion("Code"))
print(string_splosion("abc"))
print(string_splosion("ab"))