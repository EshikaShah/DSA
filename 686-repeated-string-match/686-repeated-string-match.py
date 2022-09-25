class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        t = -(-len(B) // len(A))
        return t * (B in A * t) or (t + 1) * (B in A * (t + 1)) or -1