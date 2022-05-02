class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start = 0
        end = len(A)-1
        while start < end:
            if A[start] % 2 == 0:
                start += 1
            elif A[end] % 2 != 0: # to avoid not necessary swap if the end is already odd
                end -= 1
            else:
                A[start], A[end] = A[end], A[start]
        return A
        