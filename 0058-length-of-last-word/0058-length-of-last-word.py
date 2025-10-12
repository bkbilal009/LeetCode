class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for i in s[::-1]:
            if i == " ":
                if length >= 1:
                    break
            else:
                length += 1
        return length 