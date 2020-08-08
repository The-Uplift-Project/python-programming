#Day15 Code
#Linked Lists

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
      newNode=Node(data)    #if head parameter is nobne then return new node as head
      if not head:
        return newNode #start through the head and iterate list taking head as reference
      current=head
      #check whether there is next node and then jump to that node setting by setting          #our current reference to the next code
      while current.next:
        current=current.next
        #exit when there is no next node end of the list
      current.next=newNode                # insertion at the end of the linked list
      return head                         #returns the head of the list
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
