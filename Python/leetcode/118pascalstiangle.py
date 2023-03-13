from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,numRows):
            ans.append([1]+[sum(ans[i-1][j-1:j+1]) for j in range(1,i)]+[1])
        print(ans)

Solution().generate(4)