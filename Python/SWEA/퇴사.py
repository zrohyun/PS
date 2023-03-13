N = int(input())
dp = [0]*N
sche = [tuple(map(int,input().split())) for i in range(N)]
# dp = [t for t,p in sche]

for i in range(len(dp)):
    ti,pi = sche[i]
    if i + ti > len(dp):
        continue
    log = [pi]
    for j in range(i):
        tj,pj = sche[j]
        if j + tj-1 < i:
            log.append(max(pi,dp[j] + pi))
    dp[i] = max(log)

print(max(dp))
