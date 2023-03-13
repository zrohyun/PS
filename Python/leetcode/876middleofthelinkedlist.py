# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 1
        import copy
        head2 = copy.copy(head)
        while head.next:
            cnt +=1
            head = head.next
        
        cnt = cnt//2
        for _ in range(cnt):
            head2 = head2.next
         
        #Editor sol
        # arr = [head]
        # while arr[-1].next:
        #     arr.append(arr[-1].next)
        # return arr[len(arr) // 2]
        
        #Other sol
#         def middleNode(head):
#             slow = head
#             fast = head

#             while fast and fast.next:
#                 slow = slow.next
#                 fast = fast.next.next
#             return slow


        
        return head2