class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = []

        for word in words:
            reversed_word = word[::-1]      # har word ke letters reverse karo
            reversed_words.append(reversed_word)

        return " ".join(reversed_words)
