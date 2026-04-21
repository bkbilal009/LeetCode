class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            sum = 0
            while n > 0:
                digit = n % 10
                sum = sum + (digit * digit)
                n //= 10

            return sum 

    # T:O(n)
    # S:O(1)
        slow = n
        fast = getNext(n)

        while (fast != 1) and ( slow != fast):
            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1