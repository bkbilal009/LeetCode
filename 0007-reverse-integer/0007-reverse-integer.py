class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        rev = int(str(x)[::-1]) * sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev