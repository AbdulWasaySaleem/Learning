#linked list Single and Double 
#Single linked list value and next pointer (Head)
#Double linked list value, next pointer and previous pointer (Head and Tail)

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

Head = Node(1) #Node 1
A = Node(2) #Node 2
B = Node(3) #Node 3
C = Node(4) #Node 4

# Linking nodes
Head.next = A
A.next = B
B.next = C

#Traversing the linked list - O(n) time complexity 
current = Head
while current:
  #print(current.value)
  current = current.next
  
#Displaying  
def display_linked_list(head):
  current = head
  values = []
  while current:
    values.append(current.value)
    current = current.next
  print(" -> ".join(map(str, values)))
  
display_linked_list(Head)

#Searching for a value in the linked list - O(n) time complexity
def Search_Linked_list(head, target):
  current = head 
  while current:
    if current.value == target:
      print(f"Value {target} found in the linked list.")
      return
    current = current.next
  print(f"Value {target} not found in the linked list.") 

Search_Linked_list(Head, 13)