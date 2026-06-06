class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        total_sum = sum(nums)

        result = [0] * n
        curr = 0

        for i in range(n):
            left_sum = curr

            curr += nums[i]

            right_sum = total_sum - curr

            result[i] = abs(right_sum - left_sum)

        return result