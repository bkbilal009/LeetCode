class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # Step 1: pop characters until '['
                word = ""
                while stack and stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()  # remove '['

                # Step 2: get number before '['
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                # Step 3: repeat and push back
                stack.append(word * int(num))

        return "".join(stack)
