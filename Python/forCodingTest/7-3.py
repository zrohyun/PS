def solution():
    n,m = list(map(int,input().split()))
    dduck = list(map(int, input().split()))
    s,e = 0,max(dduck)
    ans = -1
    while s<= e:
        mid = (s + e) // 2
        sliced = sum([i - mid for i in dduck if i > mid ])
        
        if sliced < m:
            
            e  = mid - 1
        else:
            ans = mid
            s = mid +1
    return ans

print(solution())
