class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in range(len(arr) -1, -1 ,-1):
            temp = arr[i]
            arr[i] = max
            max = __builtins__.max(max,temp) # max if max > temp else temp
        return arr