#모험가 길드
# N명의 모험가
# N명당 공포도 n
# 최대 구성 그룹, n 공포도의 모험가는 n명 이상의 그룹에 포함되어야 함.

N = int(input())
mem = list(map(int, input().split()))
mem.sort()

result = 0
count = 0
for i in mem:
    count +=1
    if count >= i:
        result +=1 
        count =0

print(result)