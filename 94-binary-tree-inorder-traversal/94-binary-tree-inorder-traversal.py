# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def inorder(root, l):
        #     if root:
        #         l = inorder(root.left, l)
        #         l.append(root.val)
        #         l = inorder(root.right, l)
        #     return l
        # return inorder(root, [])
        res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if(stack):
                root = stack.pop()
                res.append(root.val)
                root = root.right
            else:
                return res