# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        temp = defaultdict(int)
        temp[0] = 1

        def calc(root, prev):
            if not root:
                return 0
            prev += root.val

            ans = 0
            ans += temp[prev - targetSum]
            
            temp[prev] +=1
            
            if root.right:
                ans += calc(root.right, prev)
            if root.left:
                ans += calc(root.left, prev)
            
            temp[prev]-=1
            
            return ans
        
        return calc(root, 0)

        # return ans
