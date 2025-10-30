class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for a,b in zip(word1,word2):
            result += a + b
        result += word1[len(word2):] + word2[len(word1):]
        return result