class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        i = 0
        j = len(nums) - 1
        count = 0
        
        while i < j:
            current_sum = nums[i] + nums[j]
            
            if current_sum < target:
                count += (j - i)
                i += 1
            else:
                j -= 1
        
        return count
