# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        tree = [cloned]
        while True:
            next_level = []
            for i in tree:
                if(i.val == target.val):
                    return i
                if(i.left):
                    if(i.left.val==target.val):
                        return i.left
                    next_level.append(i.left)
                if(i.right):
                    if(i.right.val==target.val):
                        return i.right
                    next_level.append(i.right)
            tree = next_level