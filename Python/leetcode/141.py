# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        while head:
            if head.val == 'a': return True
            head.val = "a"
            head = head.next
        
        return False

"""
Other Solution using id()
class Solution(object):
    def hasCycle(self, head):

        :type head: ListNode
        :rtype: bool
        from collections import defaultdict
        dic=defaultdict(int)  #creating a dictionary for storing adresses of nodes
        node=head
        while(node):
            key= id(node)
            if dic[key]==1: #if we have already seen the address , it returns true
                return True
            else:
                dic[key]=1 # else updates it as "seen" ("1" represents seen)
                node=node.next #going to next node
        return False #if loop ends before we found any repeating adress that means there is no cycle so returns false

"""