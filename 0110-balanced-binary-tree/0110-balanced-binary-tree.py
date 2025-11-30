# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return [0, True]

            right = dfs(root.right)
            left = dfs(root.left)

            if not right[1] or not left[1]:
                return [right[0] - left[0], False] 

            if abs(right[0] - left[0]) > 1:
                return [right[0] - left[0], False]

            return [1 + max(right[0], left[0]), True]

        _, res = dfs(root)
        return res
        
        