class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        maxEl = 1

        for i in range(len(arr)):
            if i == 0:
                arr[i] = 1
            elif arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1

            maxEl = max(maxEl, arr[i])

        return maxEl