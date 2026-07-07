# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], c:int = 0) -> int:
        if not root: return c
        c += 1
        return max(self.maxDepth(root.right, c), self.maxDepth(root.left, c))