# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        s = set()
        for num in nums:
            s.add(num)

        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy

        while curr != None:
            if curr.val in s:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return dummy.next
