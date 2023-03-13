n,m = map(int, input().split())
mat = [list(map(int,input())) for i in range(n)]
def solution(mat):
    global n,m
    # n,m = len(mat),len(mat[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                ans += 1
    
    return ans

def dfs(i,j):
    global n,m
    if not (0<= i < n and 0<= j < m):
        return False
    
    if mat[i][j] == 0: 
        mat[i][j] = 1
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i,j-1)
        return True
    return False