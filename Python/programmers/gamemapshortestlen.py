from collections import deque
def solution(maps):
    answer = 0
    ylen,xlen = len(maps),len(maps[0])
    condition = lambda x,y: (0<=x<xlen and (0<=y<ylen))
    
    queue = deque([(0,0)])
    md = [(1,0),(0,1),(-1,0),(0,-1)]
    while queue:
        y,x = queue.popleft()
        nowlen = maps[y][x]
        for my,mx in md:
            if condition(x+mx,y+my):
                if maps[y+my][x+mx] == 1:
                    queue.append((y+my,x+mx))
                    maps[y+my][x+mx] = nowlen + 1
    # print(maps)
    ans = maps[ylen-1][xlen-1]
    
    return ans if ans!=1 else -1
# def dfs(y,x):
#     nowlen =maps[y][x] 
#     for my,mx in md:
#         if condition(x+mx,y+my):
#             if maps[y+my][x+mx] == 1:
#                 maps[y+my][x+mx] = nowlen + 1
#                 dfs(y+my,x+mx)
                