class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res =[0] * len(heights)

        for i in range(len(heights)):
            res[i] = heights[i]
            
        res.sort()
        count = 0

        for i in range(len(heights)):
            if heights[i] != res[i]:
                count += 1

        return count