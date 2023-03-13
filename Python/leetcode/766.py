from collections import deque
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        m,n = len(matrix), len(matrix[0])
        before = matrix[0][:-1]
        
        for i in range(1,m):
            if matrix[i][1:] == before:
                before = matrix[i][:-1]
            else:
                return False
        
    
        # deque에 하나씩 차례대로 넣는 것도 방법일듯
#         li = deque([set([i]) for i in matrix[0]])
#         for i in range(1,m):
#             li.appendleft(set([matrix[i][0]]))
#             for j in range(1,n):
#                 li[j].add(matrix[i][j])
        
#         return all([len(i)==1 for i in li])
    
#         dp = matrix[0]
        
#         for row in matrix[1:]:
#             dp.pop()
#             dp.insert(0,row[0])
#             if dp != row:
#                 return False
    