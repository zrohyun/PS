# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head

        # set point first,second node
        # set moving point even,odd
        first = odd = head
        second = even = head.next
        
        head = head.next.next
        
        while head:
            # link next odd node and move pointer
            odd.next = head
            odd = odd.next
            if head.next:
                # link next even node and move pointer
                even.next = head.next
                even = even.next
            else:
                # if no next even node, set next None
                even.next = None
                break
            
            # jump two step
            head = head.next.next

        # link last odd node to head of the odd node
        odd.next = second

        return first

