# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ppos = 0
        ppre = 0
        def calc(pre, post):
            nonlocal ppos
            nonlocal ppre
            
            if ppre >= len(pre):
                return

            cur = pre[ppre]
            ppre +=1
            
            left = None
            right = None

            if cur != post[ppos]:
                left = calc(pre, post)

            if cur != post[ppos]:
                right = calc(pre, post)

            ppos +=1
            return TreeNode(cur, left, right)

        return calc(preorder, postorder)