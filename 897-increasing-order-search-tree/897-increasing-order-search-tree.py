# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root, l):
            if root:
                l = inorder(root.left, l)
                l.append(root.val)
                l = inorder(root.right, l)
            return l
        l = inorder(root, [])
        head = TreeNode(0)
        ptr = head
        for i in l:
            ptr.right = TreeNode(i)
            ptr = ptr.right
        return head.right