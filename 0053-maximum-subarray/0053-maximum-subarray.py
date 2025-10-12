class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            # agar pichla sum negative hai, to naya subarray start karo
            currentSum = max(nums[i], currentSum + nums[i])
            # max sum update karo
            maxSum = max(maxSum, currentSum)

        return maxSum

        
       
