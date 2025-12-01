class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Gauss summation law 

        n = len(nums)
        result = n * (n + 1) // 2

        return result - sum(nums)