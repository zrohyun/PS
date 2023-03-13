def solution1():
    import sys

    N , M  = map(int,sys.stdin.readline().split())
    card = list(map(int,sys.stdin.readline().split()))

    max = 0
    for i in range(len(card)):
        for j in range(i+1,len(card)):
            for k in range(j+1,len(card)):
                if M >= (card[i] + card[j] + card[k]):
                    if max < (card[i] + card[j] + card[k]):
                        max = (card[i] + card[j] + card[k])
                        #print(i,j,k)

    return max


def solution2():
    N,M = map(int,input().split())
    card = list(map(int,input().split()))

    from itertools import combinations
    ans = 0
    for i in combinations(card,3):
        if sum(i) > M: continue

        ans = max(sum(i),ans)

    return ans

print(solution2())
