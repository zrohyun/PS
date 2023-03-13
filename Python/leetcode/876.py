# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        step1 = head

        if head.next: 
            step2 = head.next
        else:
            return head
        
        while True:
            step1 = step1.next

            if step2.next and step2.next.next:
                step2 = step2.next.next
            else:
                break
            
            
        
        return step1

