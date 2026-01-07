#Top k frequent elemnets in an array
#Example: Input: value = [1,1,1,2,2,3], k = 2, Output: [1,2]
#Example: Input: value = [1], k = 1, Output: [1]
#Example: Input: value = [1,2], k = 2, Output: [1,2]

# from collections import Counter
# value = [1,1,1,2,2,3]
# k = 2
# freq = Counter(value)
# freq = freq.most_common(k)
# print(freq)

def top_k_frequent(values, k):
    my_dict = {}
    for num in values:
        if num in my_dict:
            my_dict[num] += 1
        else:
            my_dict[num] = 1

    sorted_nums = sorted(my_dict, key=my_dict.get, reverse=True)
    top_k = sorted_nums[:k]

    return top_k

values = [1,1,1,2,2,3]
k = 2

result = top_k_frequent(values, k)
print(result)



