from sys import stdin
input= stdin.readline
def solution():
    n,m = list(map(int,input().split()))
    brands = [tuple(map(int,input().split())) for _ in range(m)]

    cheapest_pack = sorted(brands,key=lambda x: x[0])[0]
    cheapest_indi =sorted(brands,key=lambda x: x[1])[0] 
    ans = cheapest_pack[0] * (n //6)


    if cheapest_indi[1] * 6 >= cheapest_pack[0]:
        ans = cheapest_pack[0]*(n//6) + cheapest_indi[1] *(n%6) 
        if ((n%6) * cheapest_indi[1]) >=cheapest_pack[0]:
            ans = cheapest_pack[0]*(n//6 + 1)
    else:
        ans = cheapest_indi[1] *n

    return ans 

print(solution())

