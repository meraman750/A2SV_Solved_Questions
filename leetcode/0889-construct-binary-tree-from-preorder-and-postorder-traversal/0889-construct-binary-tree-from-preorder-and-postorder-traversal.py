# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pre = 0
        post = 0

        def calc(preorder, postorder):
            nonlocal pre
            nonlocal post

            temp = preorder[pre]
            pre +=1
            
            left = None
            right = None

            if temp != postorder[post]:
                left = calc(preorder, postorder)

            if temp != postorder[post]:
                right = calc(preorder, postorder)

            post +=1

            return TreeNode(temp, left, right)

        return calc(preorder, postorder)
            
