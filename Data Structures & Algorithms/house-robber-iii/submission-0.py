# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(i):
            if i is None:
                return 0
            
            elif i in memo:
                return memo[i]
            
            else:
                rob = i.val
                if i.left:
                    rob += dp(i.left.left) + dp(i.left.right)
                if i.right:
                    rob += dp(i.right.left) + dp(i.right.right)
                skip = dp(i.left) + dp(i.right)
                max_val = max(rob, skip)
                memo[i] = max_val
                return memo[i]


        return dp(root)