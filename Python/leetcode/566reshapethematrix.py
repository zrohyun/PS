class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = []
        # tmp = []
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if len(tmp) == c:
        #             ans.append(tmp)
        #             tmp=[]
        #         else:
        #             tmp.append(mat[i][j])
        # if tmp:
        #     ans.append(tmp)
        from itertools import chain
        tmp = []
        size = len(mat)*len(mat[0])
        if size != r*c: return mat
        for i in chain(*mat):
            tmp.append(i)
            if len(tmp) == c: ans.append(tmp);tmp = []
        if tmp: ans.append(tmp)
                
        print(mat)
        return ans