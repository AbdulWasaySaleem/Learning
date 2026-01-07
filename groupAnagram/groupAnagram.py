#Group anagaram words
#Example: Input: ["eat", "tea", "tan", "ate", "nat", "bat"], Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def group_anagrams(words):
    my_dict = {}

    for word in words:
        key = "".join(sorted(word))
        
        if key in my_dict:
            my_dict[key].append(word)
        else:
            my_dict[key] = [word]
  
    return list(my_dict.values())

array = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(array)
print(result)