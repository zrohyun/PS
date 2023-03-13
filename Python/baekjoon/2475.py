def solution():
    a = list(map(int,input().split()))
    ans = 0
    for i in a:
        ans = (ans + i**2) %10
    
    return ans

print(solution())