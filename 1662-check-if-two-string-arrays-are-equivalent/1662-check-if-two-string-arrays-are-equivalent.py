class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        for w in word1:
            str1 += w
        
        str2 = ""
        for w in word2:
            str2 += w
        
        if str1 == str2:
            return True
        else:
            return False