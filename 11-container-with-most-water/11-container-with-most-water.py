class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        water = 0
        while(i<j):
            water = max(water, (j-i)*min(height[i],height[j]))
            if(height[j]>height[i]):
                i+=1
            else:
                j-=1
        return water