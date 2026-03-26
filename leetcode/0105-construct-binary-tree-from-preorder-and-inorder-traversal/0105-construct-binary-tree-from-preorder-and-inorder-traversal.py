# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        def calc(ino):
            nonlocal idx

            if not ino :
                return None
            
            lam = preorder[idx]
            temp = ino.index(lam)
            idx += 1

            left = calc(ino[:temp])
            right = calc(ino[temp+1:])
            
            return TreeNode(lam, left, right)

        return calc(inorder)


             