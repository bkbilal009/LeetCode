# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dHead = ListNode(0)
        curr = dHead
        carry = 0

        while (l1 != None or l2 != None or carry != 0):
            a = l1.val if l1 != None else 0
            b = l2.val if l2 != None else 0

            total = carry + a + b
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next

        return dHead.next