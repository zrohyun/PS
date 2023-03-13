# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = Optional[ListNode]
        if list1 and list2:
            if list1.val <= list2.val:
                head = ListNode(list1.val,None)
                list1 = list1.next
            else:
                head= ListNode(list2.val,None)
                list2 = list2.next
        else:
            if list1: return list1
            else: return list2
        
        mlist = head
        while list1 and list2:
            if list1.val <= list2.val:
                mlist.next = ListNode(list1.val,None)
                list1 = list1.next
            else:
                mlist.next = ListNode(list2.val,None)
                list2 = list2.next
            mlist = mlist.next
        
        if list1:
            mlist.next = list1
        elif list2:
            mlist.next = list2

        return head

        

"""
Other solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
"""