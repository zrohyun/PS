# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.li = []
        
        def dfs(root):
            if not root: return 
            
            dfs(root.left)
            self.li.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        print(self.li)

        

    def next(self) -> int:
        return self.li.pop(0)
#         while self.li:
#             yield self.li.pop()
        
#         yield None

    def hasNext(self) -> bool:
        if self.li: return True
        else: return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


"""
other solution
https://leetcode.com/problems/binary-search-tree-iterator/discuss/1965156/Python-TC-O(1)-SC-O(h)-Generator-Solution

other solution using stack
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]) -> None:
        self._stack = []
		# initial population of the stack
		# it'll add all the nodes on the path 
		# to the most left node (the smallest)
        self._update_stack(root)
            
    def _update_stack(self, node: Optional[TreeNode]) -> None:
        # add the next nodes to the stack
        while node:
            self._stack.append(node)
            node = node.left

    def next(self) -> int:
        # on top of the stack we have the node 
		# which we need to return
        node = self._stack.pop()
        # this node doesn't have the left subtree
		# or we already visited all the nodes in the left subtree
		# so the next node should be in the right subtree
        self._update_stack(node.right)
            
        return node.val

    def hasNext(self) -> bool:
        
        return bool(self._stack)

https://leetcode.com/problems/binary-search-tree-iterator/discuss/52525/My-solutions-in-3-languages-with-Stack
"""