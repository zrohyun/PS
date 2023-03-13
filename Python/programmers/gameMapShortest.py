board = []
def solution(maps):
    global board, condition
    board = maps
    answer = 0
    condition = lambda x,y: (0<=x<len(maps[0])) and (0<=y<len(maps))
    
    answer = dfs(0,0,1)
    print(answer)
    return answer

def dfs(x,y,rout):
    print(x,y)
    global board,condition
    if y == (len(board)-1) and x == (len(board[0])-1):
        print('rout',rout)
        return rout
    md = [(1,0),(0,1),(-1,0),(0,-1)]
    ret = set()
    for dy,dx in md:
        if condition(x+dx,y+dy):
            print((x+dx,y+dy))
            if board[y+dy][x+dx]:
                board[y+dy][x+dx] = 0
                ret.add(dfs(x+dx,y+dy,rout+1))
                board[y+dy][x+dx] = 0
    print(ret) 
    return min(ret)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))