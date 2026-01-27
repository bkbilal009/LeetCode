class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        possibleZeroDups = 0
        length = len(arr) - 1

        for i in range(length + 1):
            if i > length - possibleZeroDups:
                break
            if arr[i] == 0:
                if i == length - possibleZeroDups:
                    arr[length] = 0
                    length -= 1
                    break
                possibleZeroDups += 1

        last = length - possibleZeroDups

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possibleZeroDups] = 0
                possibleZeroDups -= 1
                arr[i + possibleZeroDups] = 0
            else:
                arr[i + possibleZeroDups] = arr[i]
