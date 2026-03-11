# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        stack = []
        cur = head
        prev = dummy
        idx = prev
        while cur:
            # print(dummy)
            # print(cur.val)
            # print(stack)
            # print("---")
            while stack and cur.val > stack[-1][0]:
                idx = stack[-1][1]
                prev = idx
                stack.pop()
            idx.next = cur 
            idx = idx.next
            stack.append([cur.val, prev])
            prev = cur
            cur = cur.next
        return dummy.next