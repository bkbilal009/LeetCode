class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i in range(len(s)):
            if s.count(s[i]) == 1:  # check if character occurs only once
                return i
        return -1  # return -1 if no unique character is found
