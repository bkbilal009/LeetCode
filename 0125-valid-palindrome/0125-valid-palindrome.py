class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()

        
        cleaned = ""
        for ch in s:
            if ch.isalnum():       
                cleaned += ch      

        
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False
