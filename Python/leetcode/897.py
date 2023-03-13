# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = tail = TreeNode()
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                predecessor.right = root
                left, root.left = root.left, None
                root = left
            else:
                
                # tail.right = tail = root # 어떻게 이 코드가 아래코드가 되지?
                tail.right = root
                tail = tail.right

                root = root.right
            
        return dummy.right

"""
Solution in-Order Traversal crazy yield from not using dfs
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

"""

"""
solution relinking
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
"""

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.final = []
    def inOrder(self,root):
        if not root:
            return
        self.inOrder(root.left)
        self.final.append(root.val)
        self.inOrder(root.right)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inOrder(root)
        newNode2 = TreeNode(self.final[0],None,None)
        newNode = newNode2
        for i in range(1,len(self.final)):
            newNode.right = TreeNode(self.final[i])
            newNode = newNode.right
        return newNode2
"""