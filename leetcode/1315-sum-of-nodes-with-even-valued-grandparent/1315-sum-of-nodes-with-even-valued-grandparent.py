# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def add(root, val):
            if not root:
                return 0
            
            if val == 0:
                # print(root.val)
                return root.val
            
            ans = 0
            if root.right:
                ans += add(root.right, val-1)
            if root.left:
                ans += add(root.left, val-1)
            return ans

        def calc(root):
            if not root:
                return
            ans = 0
            if root.val % 2 == 0:
                ans += add(root, 2)

            if root.right:
                ans += calc(root.right)
            if root.left:
                ans += calc(root.left)
            return ans

        return calc(root)
            


        