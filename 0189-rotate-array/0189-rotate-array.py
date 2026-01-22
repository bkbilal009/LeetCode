class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        step = 1
        while step <= k:
            LastElement = nums.pop()
            nums.insert(0 , LastElement)
            step += 1
        return nums