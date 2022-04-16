# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        
        def traverse(root):
            nonlocal total
            if not root:
                return
            traverse(root.right)
            total += root.val
            root.val = total
            traverse(root.left)
        
        traverse(root)
        return root