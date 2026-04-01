# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def calc(nums):
            if len(nums) < 1:
                return None
            n = max(nums)
            x = nums.index(n)

            right = calc(nums[x+1:])
            left = calc(nums[:x])

            return TreeNode(n, left, right)

        return calc(nums)
            