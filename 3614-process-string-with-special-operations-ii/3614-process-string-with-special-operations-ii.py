class Solution:
    def processStr(self, s: str, k: int) -> str:

        n = len(s)

        L = 0

        for ch in s:

            if ch == "*":
                if L > 0:
                    L -= 1

            elif ch == "#":
                L *= 2

            elif ch == "%":
                continue

            else:
                L += 1

        if k >= L:
            return "."

        for i in range(n - 1, -1, -1):

            ch = s[i]

            if ch == "*":
                L += 1

            elif ch == "%":
                k = L - k - 1

            elif ch == "#":
                L //= 2

                if k >= L:
                    k -= L

            else:
                L -= 1

            if k == L:
                return ch

        return "."