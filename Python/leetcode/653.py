# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        memory = defaultdict(int)

        v = root.val
        memory[k - v] = v
        q = []
        if root.right: q.append(root.right)
        if root.left: q.append(root.left)

        while q:
            nd = q.pop()

            v = nd.val
            if v in memory:
                return True

            memory[k - v] = v

            if nr := nd.right: q.append(nr)
            if nl := nd.left: q.append(nl)

        return False


