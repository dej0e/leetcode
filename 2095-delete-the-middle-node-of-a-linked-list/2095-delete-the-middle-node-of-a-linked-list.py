# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        n = 0
        cur = head
        while cur != None:
            cur = cur.next
            n += 1
        
        m = n // 2
        prev = head
        cur = head
        while m > 0:
            prev = cur
            cur = cur.next
            m -= 1
        
        if prev:
            prev.next = cur.next
            cur.next = None
        return head

