# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(val=0, next=head)
        right = head
        for i in range(n):
            right = right.next

        left = dummy
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return dummy.next
        
