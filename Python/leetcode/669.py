# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        self.low = low
        self.high = high
        root = self.bfs(root)
        return root
        
    
    def bfs(self,root):
        
        if not root.right and not root.left: 
            if self.low<=root.val<=self.high:
                return root
            else: return None
        
        if root.val < self.low:
            root = root.right
            if root: root = self.bfs(root)
        elif self.high < root.val:
            root = root.left
            if root:root = self.bfs(root)
        else:
            if root.right:
                root.right = self.bfs(root.right)
            if root.left:
                root.left = self.bfs(root.left)
        
        # print(root)
        
        return root

"""
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root
		```
"""