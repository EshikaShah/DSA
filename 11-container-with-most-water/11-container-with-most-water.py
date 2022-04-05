class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        ans=0
        while i<j:
            h=min(height[i],height[j])
            ans=max(ans,(j-i)*h)
            while h>=height[i] and i<j:
                i+=1
            while h>=height[j] and i<j:
                j-=1
        return ans