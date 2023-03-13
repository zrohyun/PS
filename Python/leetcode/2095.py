# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    # Tortoise and hare Single Pass
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return
        t, h = head, head.next.next
        while h and h.next:
            t = t.next
            h = h.next.next
        t.next = t.next.next
        return head