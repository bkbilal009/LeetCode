class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count_zero = 0
        longest = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                count_zero += 1
                
            while count_zero > k:
                if nums[l] == 0:
                    count_zero -= 1
                l += 1
                
            longest = max(longest, r - l + 1)
        
        return longest
