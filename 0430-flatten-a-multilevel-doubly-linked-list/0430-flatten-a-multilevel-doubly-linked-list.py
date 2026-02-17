"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if (head == None):
            return None

        pHead = Node(0)
        prev = pHead

        stack = []
        stack.append(head)

        while (stack):
            curr = stack.pop()

            curr.prev = prev
            prev.next = curr

            if (curr.next != None):
                stack.append(curr.next)

            if (curr.child != None):
                stack.append(curr.child)

            prev = curr
            curr.child = None

        pHead.next.prev = None
        return pHead.next
