# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        condition
        -100 <= node.val
        """
        if depth == 1:
            return TreeNode(val, left=root)
        dummy = root

        q = [(1, dummy)]

        while q:
            d, n = q.pop()

            if d == (depth - 1):
                n.right = TreeNode(val, right=n.right)

                n.left = TreeNode(val, left=n.left)

                continue

            if n.right: q.append((d + 1, n.right))
            if n.left: q.append((d + 1, n.left))

        return root
