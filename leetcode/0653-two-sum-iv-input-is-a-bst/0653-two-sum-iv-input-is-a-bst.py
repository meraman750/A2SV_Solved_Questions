# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        arr = []

        def calc(root):
            if not root:
                return 

            arr.append(root.val)
            calc(root.right)
            calc(root.left)

        calc(root)
        
        nums = set()
        for i in arr:
            if k-i in nums:
                return True
            nums.add(i)
        return False
        