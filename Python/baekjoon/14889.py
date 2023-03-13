from itertools import combinations
def solution():
    N = int(input())
    mem = set(range(N))
    M = [list(map(int,input().split())) for _ in range(N)]
    comb = combinations(mem,N//2)
    cache = set()
    ans = 987654321

    for i in comb:
        teama = 0
        teamb = 0

        if i in cache: 
            continue

        cache.add(tuple(i))
        cache.add(tuple(mem-set(i)))

        for a1 in tuple(i):
            for a2 in tuple(i):
                if a1 == a2: continue
                teama += M[a1][a2]

        for b1 in tuple(mem - set(i)):
            for b2 in tuple(mem - set(i)):
                if b1 == b2: continue
                teamb += M[b1][b2] 
        
        ans = min(ans,abs(teama-teamb))

    return ans


print(solution())

