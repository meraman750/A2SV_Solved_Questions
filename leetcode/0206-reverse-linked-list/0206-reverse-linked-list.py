# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(-1, head)
        cur = head
        prev = None 

        if not head:
            return None
        nex = head.next

        while cur:
            cur.next = prev
            prev = cur
            cur = nex
            if cur:
                nex = cur.next
        
        return prev