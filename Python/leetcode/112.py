# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        isleaf = lambda x: (x.left == None) and (x.right == None)

        if root == None:
            return False

        # if isleaf(root) and root.val == targetSum: return True

        q = [[0, root]]

        while q:
            val, nd = q.pop()

            if isleaf(nd) and val + nd.val == targetSum:
                return True

            if n := nd.left:
                q.append([val + nd.val, n])

            if n := nd.right:
                q.append([val + nd.val, n])

        return False
