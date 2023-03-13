def solution():
    ans = []
    for _ in range(2):
        t,f,s,p,c = list(map(int,input().split()))
        ans.append(t*6+3*f+2*s+p+2*c)
    return " ".join(ans)

print(solution())