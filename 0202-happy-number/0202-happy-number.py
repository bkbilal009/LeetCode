class Solution:
    def isHappy(self, n: int) -> bool:

        def sumOfsquareOfDigits(n):
            sum = 0
            while n > 0:
                dig = n % 10
                sum = sum + (dig * dig)
                n = n // 10
            return sum

        slow = n
        fast = n

        while fast != 1:
            slow = sumOfsquareOfDigits(slow)
            fast = sumOfsquareOfDigits(sumOfsquareOfDigits(fast))

            if slow == fast:
                return False

        return True