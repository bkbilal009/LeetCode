class Solution:
    def runningSum(self, nums):
        answer = []

        for i in range(len(nums)):
            runningSum = 0
            for j in range(i + 1):
                runningSum += nums[j]

            answer.append(runningSum)

        return answer
