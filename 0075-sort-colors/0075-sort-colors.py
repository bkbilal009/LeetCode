class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        k = 0

        # T = O(n)
        # S = O(1)

        # 2  0   2   1   1   0
        # i 
        #                    j
        # k

        while (k <= j):
            if nums[k]  == 1:
                k = k + 1
            elif nums[k] == 2:
                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp
                j = j - 1
            else:
                temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                
                i = i + 1
                k = k + 1