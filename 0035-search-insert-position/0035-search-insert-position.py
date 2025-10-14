class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:          # mid se check karte hain
                return mid
            elif nums[mid] > target:
                right = mid - 1               # right ko left side le jao
            else:
                left = mid + 1                # left ko right side le jao
        return left                           # insert position return karo
