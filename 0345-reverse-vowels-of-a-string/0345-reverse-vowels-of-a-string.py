class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        x = [letter for letter in l if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
        for i in range(len(l)-1, -1, -1):
            if(l[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
                l[i] = x[0]
                del x[0]
        return ''.join(l)