#Anagrams are words or phrases formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

def is_anagram(str1, str2):
  return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"
print(is_anagram(string1, string2))
