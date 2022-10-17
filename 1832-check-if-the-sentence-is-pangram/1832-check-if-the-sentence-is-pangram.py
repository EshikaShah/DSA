from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        x = Counter(sentence)
        if(len(x)==26):
            return True
        return False