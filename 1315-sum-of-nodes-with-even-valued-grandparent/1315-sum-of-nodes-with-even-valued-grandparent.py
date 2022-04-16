# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s = 0
        tree = [root]
        while tree:
            next_level = []
            for i in tree:
                if i.val%2==0:
                    if i.left:
                        if i.left.left:
                            s+=i.left.left.val
                        if i.left.right:
                            s+=i.left.right.val
                    if i.right:
                        if i.right.left:
                            s+=i.right.left.val
                        if i.right.right:
                            s+=i.right.right.val
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            tree = next_level
        return s