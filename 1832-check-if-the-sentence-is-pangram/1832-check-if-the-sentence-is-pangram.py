class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        container = set()

        for ch in sentence:
            container.add(ch)

        return len(container) == 26