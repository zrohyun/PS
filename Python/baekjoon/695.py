from distutils.command import check


class Solution:
    from typing import List
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mxy = [(0,1),(1,0),(-1,0),(0,-1)]
        msize = 0 #-float("inf")
        ylen,xlen = len(grid),len(grid[0])
        # lambda 사용해보기

        def check_n_addQ(y,x,q):
            if grid[y][x] == 1:
                grid[y][x] = 0
                q.append((y,x))
                
        is_out_of_bound = lambda x,y: not (0<= x <xlen and 0<=y<ylen )

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                queue = []
                check_n_addQ(i,j,queue)
                
                size = 0
                while queue:
                    y,x = queue.pop()
                    size += 1
                    for mx,my in mxy:
                        if not is_out_of_bound(x+mx,y+my):
                            check_n_addQ(y+my,x+mx,queue)
                            # if grid[y+my][x+mx] == 1:
                            #     grid[y+my][x+mx] = 0
                            #     queue.append((y+my,x+mx))
                msize = max(msize,size)
        return msize

Solution().maxAreaOfIsland(grid = 
[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])