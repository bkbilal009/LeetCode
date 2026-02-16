class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        idx = -1
        max1 = -1
        max2 = -1

        for i in range(len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
                idx = i
            elif nums[i] > max2:
                max2 = nums[i]

        return idx if max1 >= 2 * max2 else -1