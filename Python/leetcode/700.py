# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = [root]
        
        while queue:
            node = queue.pop()
            if node.val == val:
                return node
            else:
                if node.right:
                    queue.append(node.right)
                
                if node.left:
                    queue.append(node.left)
        
        return None