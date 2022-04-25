
mat = [[[0]*21 for _ in range(21)] for _ in range(21)]
def solution(a,b,c):
    while True:
        # a,b,c = list(map(int,input().split()))

        if set([a,b,c]) == {-1}: return -1  # 입력 종료

        # print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
        return w(a,b,c)
    # return w(a,b,c)

def w(a,b,c):
    global mat
    if (a<=0) or (b<=0) or (c<=0):
        return 1
    if (a>20) or (b>20) or (c>20):
        mat[20][20][20] = w(20,20,20)
        return mat[20][20][20]
    
    if mat[a][b][c]:
        return mat[a][b][c]
    
    if a<b<c:
        mat[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return mat[a][b][c]


    mat[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return mat[a][b][c]

def solution2(a,b,c):
    MAX = 21
    # dp = [[[0]*MAX]*MAX for __ in range(MAX)] # wrong method no paste list like this
    dp = [[[0]*MAX for _ in range(MAX)] for __ in range(MAX)]
 
    def w(a, b, c) :
        if a<=0 or b<=0 or c<=0 :
            return 1
        if a>20 or b>20 or c>20 :
            return w(20, 20, 20)
    
        # 값이 이미 존재한다면 그 값을 바로 리턴.
        if dp[a][b][c]:
            return dp[a][b][c]
    
        if a<b<c :
            dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
            return dp[a][b][c]
    
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return dp[a][b][c]
    
    while True :

        # a, b, c = map(int, input().split())

        if a== -1 and b==-1 and c==-1 :
            # break
            return -1
        return w(a,b,c)
    
        # print("w(%d, %d, %d) = %d"%(a, b, c, w(a, b, c)))


k = []
kk = range(0,4)
for _ in range(3):
    for i in kk:
        k.append(i)

from itertools import permutations as p

for n,(a,b,c) in enumerate(list(p(k,3))):
    #print(n,end=" ")
    sol1 = solution(a,b,c) 
    sol2 = solution2(a,b,c)
    if sol1 != sol2:
        print(a,b,c)
        print(sol1,sol2)
        print()

# solution()

def solution():
    
    def w(a,b,c):

        if (a<=0) or (b<=0) or (c<=0):
            return 1
        if (a>20) or (b>20) or (c>20):
            mat[20][20][20] = w(20,20,20)
            return mat[20][20][20]
        
        if mat[a][b][c]:
            return mat[a][b][c]
        
        if a<b<c:
            mat[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
            return mat[a][b][c]


        mat[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return mat[a][b][c]

    mat = [[[0]*21 for _ in range(21)] for _ in range(21)]
    while True:
        a,b,c = map(int,input().split())
        if a==-1 and b ==-1 and c==-1: break  # 입력 종료          

        print(f"w({a}, {b}, {c}) = {w(a,b,c)}")

solution()

