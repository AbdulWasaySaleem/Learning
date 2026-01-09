#Product of element except self
# prod = 1 

# for i in range(len(array)):
#   prod = prod * array[i]

# for i in range(len(array)):
#   array[i] = prod // array[i]

# print(array)

def product_except_self(array):
    n = len(array)

    left = [1] * n
    right = [1] * n
    result = [1] * n

    #Left array values nsertion
    for i in range(1, n):
        left[i] = left[i - 1] * array[i - 1]

    #right array values insertion
    for i in range(n - 2, -1, -1): #(Start, Stop, Step) i=2-1-0
        right[i] = right[i + 1] * array[i + 1]

    #Inserting to result 
    for i in range(n):
        result[i] = left[i] * right[i]

    return result

array = [1, 2, 4, 6]
output = product_except_self(array)
print(output)
