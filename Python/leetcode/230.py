# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []    


        def bfs(root):  
            if not root: return

            bfs(root.left)
            a.append(root.val)
            bfs(root.right)
            
        bfs(root)
        return a[k-1]

"""
other solution
class Solution:
    def kthSmallest(self, root, k):
        :type root: TreeNode
        :type k: int
        :rtype: int
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]

class Solution:
    def kthSmallest(self, root, k):

        :type root: TreeNode
        :type k: int
        :rtype: int
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right   

"""