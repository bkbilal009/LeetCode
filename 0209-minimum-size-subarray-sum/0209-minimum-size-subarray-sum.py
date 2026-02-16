class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:      
        minDistance = sys.maxsize
        sum = 0
        i = 0

        for j in range(len(nums)):
            sum += nums[j]

            while sum >= target:
                minDistance = min(minDistance, j - i + 1)
                sum -= nums[i]
                i += 1

        return 0 if minDistance == sys.maxsize else minDistance