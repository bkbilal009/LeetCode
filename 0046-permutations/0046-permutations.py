class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums[:]]

        result = []
        for i in range(len(nums)):
            n = nums[i]
            remaining = nums[:i] + nums[i+1:]

            for p in self.permute(remaining):
                result.append([n] + p)
        return result
