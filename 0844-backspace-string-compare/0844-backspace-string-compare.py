class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            result = []

            for ch in string:
                if ch != '#':
                    result.append(ch)   # normal letter → add
                elif result:
                    result.pop()        # '#' → remove last letter
            return "".join(result)


        return build(s) == build(t)