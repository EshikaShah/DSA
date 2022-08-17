# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return -1
            lheight = height(root.left)
            rheight = height(root.right)
            return max(lheight, rheight) + 1
        if not root:
            return True
        h = abs(height(root.right) - height(root.left))
        return h<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)