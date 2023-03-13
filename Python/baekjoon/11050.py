from math import factorial as fac
def solution():
    n,k = list(map(int,input().split()))

    return int(fac(n)/fac(k)/fac(n-k))

print(solution())