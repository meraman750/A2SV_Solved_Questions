# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #LPR
        ans = []
        def calc(cur):
            if not cur:
                return
            calc(cur.left)
            ans.append(cur.val) 
            calc(cur.right)
        
        calc(root)
        
        return ans