# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pHead = ListNode(0)
        pHead.next = head
        prev = pHead
        curr = head

        while (curr != None):
            if (curr.val == val):
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return pHead.next