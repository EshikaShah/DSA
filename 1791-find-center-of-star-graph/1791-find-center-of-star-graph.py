class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = edges[0][0]
        b = edges[0][1]
        c = edges[1][0]
        d = edges[1][1]
        if(a==c):
            return a
        if(a==d):
            return a
        if(b==c):
            return b
        if(b==d):
            return b