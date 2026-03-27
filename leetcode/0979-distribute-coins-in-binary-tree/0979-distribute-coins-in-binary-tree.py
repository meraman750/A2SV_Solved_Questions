# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def calc(root):
            nonlocal res
            if not root:
                return [0, 0]

            left = calc(root.left)
            right = calc(root.right)
            res += abs(left[0] - left [1])
            res += abs(right[0] - right[1])

            return [1 + right[0] + left[0], root.val + right[1] + left [1]]

        calc(root)
        return res

