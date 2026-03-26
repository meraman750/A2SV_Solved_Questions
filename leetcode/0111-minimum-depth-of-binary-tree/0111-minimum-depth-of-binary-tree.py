# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def calc(root):
            if not root:
                return 0

            left = float("inf")
            right = float("inf")

            if root.left:
                left = calc(root.left)
            if root.right:
                right = calc(root.right)

            return 1 + min(left, right) if 1 + min(left, right) != float("inf") else 1

        return calc(root)