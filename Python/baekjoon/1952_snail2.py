M,N = map(int,input().split())

# 쌓인 col,row의 layer의 수만큼 방향전환이 이루어지기 때문에 굳이 시뮬레이션할 필요없음.
if (M == N) or (M < N):
    ans = M*2 -2
else: # if M > N, row > col이라면 row < col일때와는 다르게 마지막에 한 번 더 꺾는 전환이 생기게 된다.
    ans = N * 2 -1

print(ans)