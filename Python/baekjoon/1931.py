def solution():
    N = int(input())
    seminar = [tuple(map(int,input().split())) for _ in range(N)]
    seminar = sorted(seminar, key= lambda x: (x[1],x[0]))

    ans = 1
    end = seminar[0][1]
    for (s,e) in seminar[1:]:
        if s>=end:
            ans +=1
            end = e
    
    return ans

print(solution())