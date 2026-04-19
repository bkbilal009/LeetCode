# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        len = 0
        l = head

        while (l != None):
            len = len + 1
            l = l.next

        d = len - n + 1

        prev = dummy
        curr = head

        i = 0
        while ( i < (d - 1)):
            curr = curr.next 
            prev = prev.next
            i = i + 1
            
        prev.next = prev.next.next

        return dummy.next

        # T = O(n)
        # S = O(1)

        # 1  2  3  4  5
        # p  c 
        # d = 4
        # 3