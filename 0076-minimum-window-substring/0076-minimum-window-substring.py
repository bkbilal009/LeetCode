class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need = Counter(t)
        have = {}
        left = 0
        match = 0
        res = ""

        for right in range(len(s)):
            ch = s[right]
            have[ch] = have.get(ch, 0) + 1
            if ch in need and have[ch] == need[ch]:
                match += 1

            while match == len(need):
                temp = s[left:right+1]
                if not res or len(temp) < len(res):
                    res = temp
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    match -= 1
                left += 1

        return res