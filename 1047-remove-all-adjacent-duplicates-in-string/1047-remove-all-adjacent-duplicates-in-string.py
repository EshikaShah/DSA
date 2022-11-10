from collections import Counter
class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        for ch in s:
            if l and l[-1] == ch:
                l.pop()
            else:
                l.append(ch)
        return "".join(l)