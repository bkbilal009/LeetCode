class Solution:
    def maxTotalValue(self, nums, k):
        
        maxEl = nums[0]
        minEl = nums[0]
        
        for num in nums:
            maxEl = max(maxEl, num)
            minEl = min(minEl, num)
        
        return (maxEl - minEl) * k