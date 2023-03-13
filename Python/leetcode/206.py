# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        """
        What the fucking one line solution
        last = None
        while head:
            last, head.next, head = head, last, head.next
            # i think the last variables processed sequently
            # head -> head.next -> last
        return last
        """
        
        ans = None
        
        if not head: return ans
        
        while head:
            tmp = head
            head = head.next
            tmp.next = ans
            ans = tmp

        return ans

"""
Other solution

XII_012's avatar
XII_012
0
April 11, 2022 4:18 PM

72 VIEWS

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursion
        # base case
        if not head or not head.next:  # avoid the empty input
            return head
        
        # common case
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return res
        # T.C.: O(N)
        # S.C.: O(N)
        
        # Iterative
        pre, curr = None, head
        while curr:
            temp = curr.next
            curr.next = pre
            curr, pre = temp, curr
        return pre
        # T.C.: O(N)
        # S.C.: O(1)
        # maybe time complexity and space complexity
"""
