# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def maxh(node,c):
            if not node: return c
            c+=1
            print(node.val,c)
            return max(maxh(node.right,c),maxh(node.left,c))
        #iteration
        def dfs(root):
            if not root : return True
            if abs(maxh(root.right,0)-maxh(root.left,0)) <= 1:
                return dfs(root.right) and dfs(root.left)
            else:
                return False
        return dfs(root)
            


