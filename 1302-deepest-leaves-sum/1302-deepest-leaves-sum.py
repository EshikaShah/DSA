# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        tree=[root]
        while True:
            next_level=[]
            for i in tree:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            if not next_level:
                return sum([j.val for j in tree])
            tree=next_level