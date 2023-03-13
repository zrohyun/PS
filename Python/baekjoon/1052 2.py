from math import log2

# 2의 거듭제곱의 숫자 타일을
# 곱하는 게임과 원리는 같은 것 같다.
def solution():
    n,k = list(map(int,input().split()))
    save = []

    # 2의 거듭제곱을 모두 추출
    while int(log2(n)) >= 1:
        save.append(2**int(log2(n)))
        n -= 2 ** int(log2(n))
        if n == 0: break
    
    if n: save.append(n)

    # 거듭제곱으로 추출된 길이가 k보다 짧으면
    # 분리해서 k개만큼 만드는 것이 가능하다.
    if bin(n).count('1') < K:#len(save) < k:
        return 0

    # k-1개의 제일 큰 2의 거듭제곱들은 놔두고 그 외의 것들을
    # 1개로 합쳐주는 작업이 필요
    save = save[k-1:][::-1]


    ans = 0
    minimum = save[0]

    # 제일 작은 물병부터 하나씩
    # 합쳐나간다. 그 과정에서 예를들어 [4,1]이라면 
    # 합칠때 3개의 병이 추가로 필요하다.[8,2]면 6병
    for i in save[1:]:
        ans += i - minimum
        minimum = i*2
    
    return ans
    


solution()

## other solution
# 비트마스킹 사용

# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())
# temp = N
"""
거꾸로 2의 거듭제곱을 더해가며 K개 이하로 1
즉, 2의 거듭제곱(물병)이 생길때까지 연산 수행
"""
# while bin(temp).count('1') > K:
#     temp += 2 ** (bin(temp)[::-1].index('1'))
# print(temp-N)