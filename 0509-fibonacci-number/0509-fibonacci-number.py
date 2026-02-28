class Solution:
    def fib(self, n: int) -> int:
        map = {}

        def helper(n):
            if n in map:
                return map[n]

            if n <= 1:
                return n

            res = helper(n-1) + helper(n-2)
            map[n] = res
            return res

        return helper(n)