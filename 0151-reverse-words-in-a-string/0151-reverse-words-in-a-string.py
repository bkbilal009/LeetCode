class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        l = 0
        r = n - 1

        # remove leading spaces
        while l < n and s[l] == " ":
            l += 1

        # remove trailing spaces
        while r >= 0 and s[r] == " ":
            r -= 1

        sb = []   # StringBuilder ki jagah list

        # remove extra spaces in between
        while l <= r:
            if s[l] != " ":
                sb.append(s[l])
            else:
                if sb[-1] != " ":
                    sb.append(" ")
            l += 1

        # reverse whole string
        sb.reverse()

        start = 0
        n = len(sb)

        # reverse each word
        for end in range(n + 1):
            if end == n or sb[end] == " ":
                p1 = start
                p2 = end - 1

                while p1 < p2:
                    sb[p1], sb[p2] = sb[p2], sb[p1]
                    p1 += 1
                    p2 -= 1

                start = end + 1

        return "".join(sb)
