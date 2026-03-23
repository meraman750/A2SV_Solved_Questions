# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def calc(roota, rootb):
            if not roota and not rootb:
                return True
            elif roota and not rootb:
                return False
            elif rootb and not roota:
                return False
            if roota.val != rootb.val:
                return False

            return calc(roota.left, rootb.left) and calc(roota.right, rootb.right)

        return calc(q, p)