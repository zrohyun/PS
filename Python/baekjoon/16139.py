import sys

input = sys.stdin.readline

name = input().strip()
n = int(input())

# accummulate sum
arr = [[0 for i in range(26)] for i in range(len(name))]

arr[0][ord(name[0]) - 97] = 1

for i in range(1, len(name)):
    arr[i][ord(name[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]

for i in range(n):
    a = input().split()
    if int(a[1]) > 0:
        res = arr[int(
            a[2])][ord(a[0]) - 97] - arr[int(a[1]) - 1][ord(a[0]) - 97]
    else:
        res = arr[int(a[2])][ord(a[0]) - 97]
    print(res)
"""
TLE
26밖에 되지 않는 작은 공간에서는 dict를 써서
hashing하는 게 오히려 오버헤드 인지도..?
"""
#import sys
#from collections import defaultdict, deque
#from copy import deepcopy as dcp
#from typing import List
#
#input = sys.stdin.readline
#def solution():
#	"""인간-컴퓨터 상호작용"""
#	S = str(input().rstrip())
#	q = int(input()) # query num
#
#	ch_pnt = [defaultdict(int)] * (len(S)+1) # check point
#	cnt_S(S,ch_pnt)
#	#print(ch_pnt)
#
#	for _ in range(q):
#		alpha, st,end = map(str,input().split())
#		st,end = int(st), int(end)+1
#		print(ch_pnt[end][alpha] - ch_pnt[st][alpha])
#
#	
#
#def cnt_S(S: str, ch_pnt: List[dict]):
#	cnt = defaultdict(int)
#	for n,i in enumerate(S,start=1):
#		cnt[i] +=1
#		#do not copy dict cause TLE
#		#ch_pnt[n] = dcp(cnt)
#		#ch_pnt[n] = defaultdict({k:v for k,v in cnt.items()})
#		tmp = defaultdict(int)
#		for k,v in cnt.items():
#			tmp[k] += v
#		ch_pnt[n] = tmp
#
#	
#
#solution()

