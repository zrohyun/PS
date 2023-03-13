# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.bfs(root,0)
        return root
    
    def bfs(self,root,right_branch):
        if not root: return 0
        
        left,right = 0,0
        val = root.val
        if root.right: right = self.bfs(root.right,right_branch)
            
        if right_branch: root.val += (right+right_branch)
        else:
            root.val += right
        
        if root.left: left = self.bfs(root.left,root.val)
        
        
        
        return right + left + val

"""
other soltuion
	def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root, s):
            if not root: return s
            root.val += traverse(root.right, s)
            return traverse(root.left, root.val)
        traverse(root, 0)
        return root
"""

"""
def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        _sum = self.convert(root, 0)
        return root
        
    def convert(self, root, _sum):
        if root.right:
            _sum = self.convert(root.right, _sum)

        _sum += root.val
        root.val = _sum
        
        if root.left:
            _sum = self.convert(root.left, _sum)  
        return _sum
"""