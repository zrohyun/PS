def solution():
    n = int(input())
    parts = list(map(int, input().split()))
    m = int(input())
    req = list(map(int, input().split()))

    ans = []
    for r in req:
        s,e = 0,n-1
        while s<= e:
            mid = (s+e)//2
            if parts[mid] == r:
                ans.append(1)
                break
            
            if parts[mid] < r:
                s = mid +1
            else:
                e = mid-1
        if e<s:
            ans.append(0)
    
    return ans

print(solution())
