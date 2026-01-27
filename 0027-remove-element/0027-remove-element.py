class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Approch 1
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        return n

        
        
        # Approch 2
       # i = 0

       # for j in range(len(nums)):
        #    if nums[j] != val:
        #        nums[i] = nums[j]
         #       i += 1

       # return i

       
        