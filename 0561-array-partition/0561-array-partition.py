class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        k = 10000
        countArr = [0] * (2 * k + 1)

        for i in range(len(nums)):
            countArr[nums[i] + k] += 1

        isEvenIndex = True
        maxSum = 0

        for i in range(len(countArr)):
            while countArr[i] > 0:
                if isEvenIndex:
                    maxSum += i - k
                countArr[i] -= 1
                isEvenIndex = not isEvenIndex

        return maxSum
