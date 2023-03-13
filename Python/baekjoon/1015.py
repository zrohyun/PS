def solution():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(range(n), key = lambda x: a[x])
    # print(a)
    p = [0]*n
    for n,i in enumerate(a):
        p[i] = n
    
    return list(map(str,p))

print(" ".join(solution()))