# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        K = k
        def recur(root):
            nonlocal K
            if root==None: 
                return -1
            ls = recur(root.left)
            if ls!=-1: 
                return ls
            K-=1
            if K==0: return root.val
            return recur(root.right)
        return recur(root)
            