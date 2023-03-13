from collections import deque as dq
m = dq()

def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):

        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 가장 긴 A 연속 문자열
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신    
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    answer += min_move
    return answer

def solution(name):
    global m
    m = dq(list(name))
    print(m)
    find()

    # A가 아닌 것들의 index tuple을 구한다.(순서)
    # (1,-1) 앞 뒤 방향의 index tuple만큼의 데카르트 곱을 계산한다.
    # 마냑 index 길이가 5라면 2^5 만큼의 곱집합이 나온다.
    # 모든 곱집합 케이스에 대해 min값을 구한다.
    # 혹은 deque rotate 연산으로 재귀로 할 수도 있을 듯 하다.

def find():
    global m
    print(m)
    if set(m) == set(["A"]):
        return 0
    n = 1
    while True:
        m.rotate(1)
        print(m)
        if m[0] != 'A': 
            # char = m.pop_left()
            # m.push_left("A")
            # rotate num + joystick num + left arr
            break
        n+=1
    m.rotate(-n)
    print(m)
    n = 1
    while True:
        m.rotate(-1)
        print(m)
        if m[0] != 'A': break
        n+=1
    print(m)
    m.rotate(-n)



    # A가 아니면 조이스틱 횟수
    # A면 그냥 지나감
    # while True:
    #     print(name)
    #     if set(name) == {'A'}:
    #         break

    #     m = 1
    #     l,r = n-(m%len(name)),(n+m)%len(name)
    #     while True:
    #         print(l,r,m,n,answer)
    #         if name[r] != 'A': 
    #             n = r
    #             answer += m
    #             break
    #         elif name[l] != 'A':
    #             n = l
    #             answer += m
    #             break
    #         m+=1
    #         l,r = n-(m%len(name)),(n+m)%len(name) 
        


    #     answer += min(ord(name[n]) - ord('A') , ord("Z")-ord(name[n])+1)
    #     name[n] = 'A'
    
    
    
    # return answer
"""
from collections import deque
from itertools import product

def solution(name):    
    results = []

    for rs in product((-1,1), repeat=len(name)-1):
        name_deque = deque(name)
        default = deque('A'*len(name))

        for c, r in enumerate([0]+list(rs)):
            default.rotate(r)
            name_deque.rotate(r)
            default[0] = name_deque[0]

            if name_deque == default:
                results.append(c)
                break

    return min(set(results))+sum([min(ord(l)-ord('A'), ord('Z')-ord(l)+1) for l in name])
"""
#https://velog.io/@jqdjhy/프로그래머스-파이썬-조이스틱-Greedy