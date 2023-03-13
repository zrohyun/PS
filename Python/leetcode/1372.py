# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        stack = [(root,0,0)]
        res = 0
        while stack:
            r,left,right = stack.pop()
            res = max(res,left,right)
            if r.left: stack.append((r.left,right+1,0))
            if r.right: stack.append((r.right,0,left+1))
        
        return res
            
        
#         res = 0
#         def dfs(root, direction,num):
#             nonlocal res
            
            
#             res = max(res,num)
            
#             if not (root.left or root.right): return
            
#             if root.left: dfs(root.left,'l', num +1 if 'l' != direction else 0)
#             if root.right: dfs(root.right,'r', num+1 if 'r' != direction else 0)
            
            
# #             if not (root.right) and not(root.left): 
# #                 res = max(res,num-1) 
# #                 return 0

# #             if root.left: ans = max(ans, dfs(root.left,'l',num+1 if 'l' != direction else 0)+ int('l' != direction))
# #             if root.right: ans = max(ans, dfs(root.right,'r',num+1 if 'l' != direction else 0) + int('r' != direction))
            
#         if not root:
#             return root
#         else:
#             ans = 0
#             if root.right:
#                 dfs(root.right,'r',1)
            
#             if root.left:
#                 dfs(root.left,'l',1)

#         return res
        


"""
Iteration Other SOlution


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root: return res
        q= deque() # node, isLeft, depth
        if root.left: 
            q.append((root.left,True,1))
        if root.right:
            q.append((root.right, False,1))
        
        while q:
            node,isleft,depth = q.popleft()
            res = max(res,depth)
            if isleft:
                if node.right: 
                    q.append((node.right,False,depth+1))
                if node.left:
                    q.append((node.left,True,1))
                
            else:
                if node.left:
                    q.append((node.left,True,depth+1))
                if node.right:
                    q.append((node.right,False,1))
        return res
""" 
"""
Recursion Solution

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root.left,True,1)
        self.dfs(root.right,False,1)
        return self.res
    
    def dfs(self,node,isLeft,depth):
        if not node: return
        self.res = max(self.res,depth)
        
        if isLeft:
            self.dfs(node.left,True,1)
            self.dfs(node.right,False,depth+1)
        else:
            self.dfs(node.left,True,depth+1)
            self.dfs(node.right,False,1)
"""
