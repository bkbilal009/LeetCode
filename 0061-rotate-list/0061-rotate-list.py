# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head

        tail = None
        size = 0
        curr = head
        
        while (curr != None):
            tail = curr
            curr = curr.next
            size += 1

        newK = k % size 
        if newK == 0:          
            return head
        diff = size - newK
        curr = head

        i = 0
        while(i < diff - 1):
            curr = curr.next
            i += 1

        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead