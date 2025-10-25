# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        # move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # if fast is None, remove the head
        if not fast:
            return head.next

        # move both until fast reaches last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # delete the nth node from end
        delNode = slow.next
        slow.next = slow.next.next
        delNode = None

        return head

