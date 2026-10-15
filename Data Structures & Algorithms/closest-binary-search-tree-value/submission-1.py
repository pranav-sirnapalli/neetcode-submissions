# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val

        def dfs(node):
            nonlocal res

            if not node:
                return

            if abs(node.val - target) < abs(res - target):
                res = node.val
            elif abs(node.val - target) == abs(res - target):
                res = min(res, node.val)

            if node.val < target:
                dfs(node.right)
            elif node.val > target:
                dfs(node.left)

        dfs(root)
        return res