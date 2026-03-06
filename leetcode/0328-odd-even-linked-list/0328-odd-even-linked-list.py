# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        if not head.next:
            return head

        dummy = head.next
        cur = head
        even_last = head
        odd_last = dummy

        count = 0
        while cur:
            if count > 1:
                if count % 2 == 0:
                    even_last.next = cur
                    even_last = even_last.next 
                else:
                    odd_last.next = cur
                    odd_last = odd_last.next

            cur = cur.next
            count+=1

        odd_last.next = None
        even_last.next = dummy
        return head