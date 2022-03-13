# -*- coding: utf-8 -*- 
# 출력형태: 나선 배열 출력
import pprint


# 1 2 1
# 2 3 2
# 1 2 1

# 1 2 3 4 1
# 4 5 6 5 2
# 3 4 7 4 3
# 2 5 6 5 4
# 1 4 3 2 1

# solution 3 -> To turn when occur out_of_bound strategy - not good

# solution 2 -> preprocessing strategy
from calendar import c
import copy

# right, down, left, up
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def solution(n, clockwise):
    answer = [[0]*n for i in range(n)]

    seq_list = preprocessing(clockwise)
    

    # 시계방향 돌아가며 삽입
    for i in range(len(seq_list)):
           
        insert_value(answer,seq_list,i)
        
    return answer

def preprocessing(clockwise):
    seq_list = []
    start = 1
    # 사용 리스트 계산 (수평방향 list)
    for i in range(n):
        
        a = list(range(start, start + n - 2*i - 1))
        
        if len(a) != 1: a.append(start)

        seq_list.append(a)
        
        # last layer case
        if len(a) == 1: break
        
        start = (start + (n-1) - 2*i)
    
    # 리버스 필요시
    if not clockwise:
        for i in range(len(seq_list)):
            seq_list[i] = list(reversed(seq_list[i]))
    return seq_list

def insert_value(answer,seq_list, i):
    # start coordinate (i,i)
    x = copy.deepcopy(i)
    y = copy.deepcopy(i)

    for j in range(4): # 4 direction(right,left,up,down)
                
        index = 0
        while ((x < n-i) and (x > -1 + i) and (y < n-i) and (y > -1 + i)):
            if len(seq_list[i]) == 1: 
                answer[y][x] = seq_list[i][0]
            else:
                answer[y][x] = seq_list[i][index]
            x += dx[j]; y += dy[j]
            index += 1

        x -= dx[j]; y -= dy[j]


for n in range(1,10):
    arr = solution(n, True)
    s = len(str(arr[len(arr)//2][len(arr)//2]))
    for i in arr:
        for j in i:
            print(f"{j:^{s}}", end=' ')
        print()
    print()

    