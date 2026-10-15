# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]

        while stack:
            node = stack.pop()

            if not node:
                continue
            
            if (node.left and not node.right):
                res.append(node.left.val)
            
            if (not node.left and node.right):
                res.append(node.right.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res