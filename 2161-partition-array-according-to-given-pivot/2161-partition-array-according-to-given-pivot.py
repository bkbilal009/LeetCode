class Solution:
    def pivotArray(self, nums, pivot):
        
        small = []
        equal = []
        greater = []
        
        for num in nums:
            
            if num < pivot:
                small.append(num)
            
            elif num == pivot:
                equal.append(num)
            
            else:
                greater.append(num)
        
        return small + equal + greater