# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        Condition
        number of nodes in the tree [0,5000]
        -1000<=n.val, targetSum<=1000
        '''
        ans = []       
        queue = []
        
        if not root:
            return ans
        
        queue.append([0,root,[]])
        
        while queue:
            v,n,p = queue.pop()
            
            is_leaf = (n.right == None and n.left == None)
            
            if (v+n.val == targetSum) and is_leaf:
                ans.append(p + [n.val])
                continue
            
            if n.right:
                queue.append([v+n.val,n.right,p+[n.val]])
            
            if n.left:
                queue.append([v+n.val,n.left, p+[n.val]])
            
            #print(queue)
        
        return ans
            