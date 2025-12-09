#Arrays are mutable
#Static and Dynamic Arrays 
#By Default Python array are Dynamic in nature (Behind the scene work same as static array but can resize itself when needed), insertion on middle are O(n) and appending at end is amortized *O(1) time complexity
arr = [5,6,8,9]

#Inserting an element - O(n) time complexity
arr.append(10)
print(arr)

#Deleting an element - O(n) time complexity
arr.remove(6)
print(arr)

#Inserting at specific index - O(n) time complexity
arr.insert(1,7) #Inserting 7 at index 1
print(arr)

#Finding an element - O(1) time complexity
print(arr[2]) 