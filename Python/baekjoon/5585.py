def solution():
    m = 1000 - int(input())
    changes = [500,100,50,10,5,1]

    ans = 0

    for i in changes:
        ans += m //i
        m = m%i
    
    return ans

print(solution())