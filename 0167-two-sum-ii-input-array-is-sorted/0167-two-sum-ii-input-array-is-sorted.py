class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
    
    # T = O(n)
    # S = O(1)
        while ( i < j):
            sum = numbers[i] + numbers[j]

            if (sum > target):
                j = j - 1

            elif (sum < target):
                i = i + 1
            
            else:
                return [i + 1 , j + 1]
