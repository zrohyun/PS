# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = head
        
        while dummy:
            if dummy.next and dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        
        
        if head and head.val == val:
            return head.next
        else:
            return head
        