# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1,v2  = [],[]
        while l1:
            v1.append(l1.val)
            l1 = l1.next
        while l2:
            v2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        l = []
        while v1 or v2:
            _sum = carry
            if v1:
                _sum += v1[0]
                v1 = v1[1:]
            if v2:
                _sum += v2[0]
                v2 = v2[1:]
            carry = int(_sum/10)
            l.append(_sum%10)
        
        if carry: l.append(carry)
            
        ans = ListNode(-1,None)
        cur = ans
        for i in l:
            cur.next = ListNode(i,None)
            cur = cur.next
        
        return ans.next
        
        
        
    
    def addTwoNumbers_v1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        while 한번으로 두 node를 같이 꺼내게 되면 모든 while에서 조건문 검사가 필요함
        매 반복마다 조건 검사는 시간이 많이 드나..?
        '''
        ans = ListNode(val=-1)
        cur = ans
        cout = 0
        while True:
            _sum = 0
            if l1 == None and l2 == None: break
            
            elif l1 ==None:
                _sum += l2.val+cout
                l2 = l2.next
            
            elif l2 == None:
                _sum = l1.val + cout
                l1 = l1.next
            else:
                _sum = l1.val + l2.val + cout
                l1 = l1.next
                l2 = l2.next
        
            
            cur.next = ListNode(_sum%10,None)
            cur = cur.next
            cout = int(_sum/10)
        
        if cout:
            cur.next = ListNode(cout,None)
            

        
        return ans.next
