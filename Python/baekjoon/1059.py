from itertools import combinations as combi
from sys import stdin
input = stdin.readline

def solution():
    N = int(input().strip())
    S = [0] + sorted(list(map(int, input().split())))
    n = int(input().strip())

    fromto = 0
    for i in range(len(S)-1):
        if S[i] < n < S[i+1]:
            fromto= list(range(S[i]+1, S[i+1]))
            break
    
    if fromto == 0: 
        return 0

    n_idx = fromto.index(n)
    # n을 기준으로 수를 나누어 a*b의 경우의 수로 계산 가능 -1 (n,n으로 동시 조합된 경우 제외)
    return (n_idx+1)*(len(fromto)- n_idx)-1
    # return len(list(combi(fromto,2)))-len(list(combi(fromto[n_idx+1:],2))) - len(list(combi(fromto[:n_idx],2)))
    
    #other solution
    # 다른 풀이를 보려고 블로그 몇개를 봤는데 전부 이 식으로 결과를 냈다.
    # 뭐 정답은 맞았겠으나 조합으로 생각하는 게 편할텐데 어떻게 이런 식이 나왔지?
    #(n - s) * (e - n + 1) + (e - n);

print(solution())
