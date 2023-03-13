from copy import deepcopy
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp_prior = deepcopy(matrix[0])
        dp_post = [0]*len(matrix[0])
        # print(matrix)
        for i in range(1,len(matrix)):

            for j in range(len(matrix)):
                if 0 < j < len(matrix)-1: # 조건 모두 충족
                    dp_post[j] = matrix[i][j] + min(dp_prior[j-1:j+2])
                elif 0 < j : # 위의 조건 불충족, 왼쪽 공간만 있음
                    dp_post[j] = matrix[i][j] + min(dp_prior[j-1:j+1])
                elif j < len(matrix)-1: # 오른쪽 공간만 있음
                    dp_post[j] = matrix[i][j] + min(dp_prior[j:j+2])
                else: #위의 조건 모두 불충족 1줄밖에 없음
                    dp_post[j] = matrix[i][j] + min(dp_prior[j])
            
            dp_prior = dp_post
            dp_post = [0]* len(matrix[0])
            # print(dp_prior)
            # print(dp_post)
        
        return min(dp_prior)

