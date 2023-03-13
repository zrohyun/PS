# from collections import defaultdict

# candidates = defaultdict(int)

# N,M,K = map(int,input().split())

# for i in [2,3,1]:
# 	for j in list(map(int,input().split())):
# 		candidates[j] += i

# vmax = max(candidates.values())
# kmin = 1e10
# for k,v in candidates.items():
# 	if v == vmax:
# 		kmin = min(k,kmin)
# print(kmin)

"""
번호가 더 앞에 있다는 말이 어이가 없네
정답이 뜨지 않는 걸 보니 번호가 더 앞에있다는 말이 더 번호가 작다는 말이 아닌 거 같다
개빡친다.
"""
from sys import stdin

# O(n)
input = stdin.readline
n, m, k = map(int, input().split())
candidates = {str(i): 0 for i in range(1, 4235)}
weight = [2, 3, 1]
for w in weight:
    vote = input().split()
    for i in vote:
        candidates[i] += w
winner = 0
win_vote = 0
for i in candidates:
    if candidates[i] > win_vote:
        win_vote = candidates[i]
        winner = i
print(winner)
