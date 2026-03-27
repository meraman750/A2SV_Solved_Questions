# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def calc(root):
            if not root:
                return [True, 0]
            
            left = [True, 0]
            right = [True, 0]

            if root.left:
                left = calc(root.left)
                if not left[0]:
                    return left
            if root.right:
                right = calc(root.right)
                if not right[0]:
                    return right
            temp = True if abs(left[1]-right[1]) <= 1 else False 
            return [temp, 1 + max(left[1], right[1])]

        return (calc(root))[0]