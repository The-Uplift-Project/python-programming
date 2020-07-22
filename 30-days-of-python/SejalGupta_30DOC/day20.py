#remove linked list elements

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ret = None
        while head:
            if not ret and head.val != val:             
                ret = head
            if head.next and head.next.val == val:      
                head.next = head.next.next
            else:                                       
                head = head.next
        return ret
        