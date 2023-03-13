# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ans = ListNode(0)
        ans.next = head
        s = e = ans
        
        for i in range(n):
            e = e.next
        while e.next:
            s, e = s.next, e.next
        s.next = s.next.next
        return ans.next

        