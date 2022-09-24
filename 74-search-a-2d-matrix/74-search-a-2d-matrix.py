class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if(target<=matrix[i][-1]):
                break
        arr = matrix[i]
        l = 0
        r = len(arr)-1
        while(l<=r):
            mid = (l+r)//2
            if(target == arr[mid]): return True
            elif(target<arr[mid]): r = mid-1
            else: l = mid+1
        return False