# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        vals.sort()
        dummy = cur = ListNode(0)
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next
