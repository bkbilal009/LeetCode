class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == "(":
                stack.append(")")

            elif ch == "{":
                stack.append("}")

            elif ch == "[":
                stack.append("]")
                
            else:  # closing bracket
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != ch:
                    return False

        # end of loop
        return len(stack) == 0
