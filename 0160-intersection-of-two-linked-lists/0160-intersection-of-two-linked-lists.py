# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):

        currA = headA
        currB = headB

        lenA = 0
        lenB = 0

        while (currA != None):
            lenA += 1
            currA = currA.next

        while (currB != None):
            lenB += 1
            currB = currB.next

        dif = abs(lenA - lenB)

        currA = headA
        currB = headB

        if (lenA > lenB):
            i = 0
            while (i < dif):
                currA = currA.next
                i += 1
        else:
            i = 0
            while (i < dif):
                currB = currB.next
                i += 1

        while (currA != currB):
            currA = currA.next
            currB = currB.next

        return currA