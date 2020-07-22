#Flatten a multilevel doubly linked list

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return (head)
        h = head
        while (h):
            if not h.child:
                h = h.next
                continue
            t = h.child
            while t.next:
                t = t.next
            t.next = h.next
            if h.next:
                h.next.prev = t
            h.next = h.child
            h.child.prev = h
            h.child = None
        return (head)
        