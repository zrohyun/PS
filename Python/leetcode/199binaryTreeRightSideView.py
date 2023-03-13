#https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        if not root: return ans
        
        queue = [(root,0)]
        maxlevel = -1
        while queue:
            nroot,nlevel = queue.pop()
            
            
            if maxlevel < nlevel:
                ans.append(nroot.val)
                maxlevel = nlevel
            
            
            if nroot.left:
                queue.append((nroot.left,nlevel+1))
            if nroot.right:
                queue.append((nroot.right,nlevel+1))
            
             
        return ans