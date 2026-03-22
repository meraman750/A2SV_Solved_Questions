# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def minVal(node):
            cur = node

            while cur.left:
                cur = cur.left
            return cur

        def calc(root, key):
            if not root:
                return None

            if key < root.val:
                root.left = calc(root.left, key)
            elif key > root.val:
                root.right = calc(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                temp = minVal(root.right)
                root.val = temp.val
                root.right = calc(root.right, temp.val)
            return root

        return calc(root, key)
        

        

