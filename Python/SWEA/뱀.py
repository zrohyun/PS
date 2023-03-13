def get_data():
    N = int(input())
    b = [[0]*N for _ in range(N)]
    K = int(input())
    dx = []
    for i in range(K):
        r,c = map(int,input().split())
        b[r-1][c-1] = 1

    l = int(input())
    d_informs = []
    for i in range(l):
        tmp =  list(input().split())
        x,c = int(tmp[0]), str(tmp[1])
        d_informs.append((x,c))
    # print(directions)

    return N,b,d_informs


def check(r,c,b,N):
    """check boundary"""

    if ( 0 <= r < N ) and ( 0 <= c < N ):
        if b[r][c] == 2:
            return False
        return True

    return False

# L - left ,D - right
ND = {
    "U":{
        "L":(0,-1),
        "F":(-1,0),
        "D":(0,1)
    },
    "R":{
            "L":(-1,0),
            "F":(0,1),
            "D":(1,0)
        },
    "D":{
            "L":(0,1),
            "F":(1,0),
            "D":(0,-1)
        },
    "L":{
            "L":(1,0),
            "F":(0,-1),
            "D":(-1,0)
        },
}
def check_apple(r,c,b):
    if b[r][c] == 1:
        b[r][c] = 0
        return True

    return False

def remove_tail(r,c,b):
    b[r][c] = 0

def turn(d,C):
    if C == 'D':
        d = ( d+ 1)%4
    elif C == "L":
        d = (d-1+4)%4
    return d

Ds = ["R","D","L","U"]

from collections import deque
def solution():
    N,b,d_informs = get_data()

    # snake position init
    head = deque([(0, 0)])
    b[0][0] = 2
    hd = 0 # head direction


    ans = 0 # elapsed time
    for i in range(len(d_informs)+1):
        X,C = d_informs[i] if i != len(d_informs) else (N+ans+1,"L")
        CD = ND[Ds[hd]] #current direction
        du = X-ans
        for x in range(du):
            ans+=1
            hr,hc = head[0]
            hr = hr + CD['F'][0]
            hc = hc + CD["F"][1]

            # 벽 혹은 몸과 부딪혔을 때
            if not check(hr,hc,b,N):
                return ans

            # 사과가 없을 때
            if not check_apple(hr,hc,b):
                tr,tc = head.pop()
                remove_tail(tr,tc,b)


            # 머리 들이밀기
            head.appendleft((hr, hc))
            b[hr][hc] = 2

        hd = turn(hd,C)




    return ans

print(solution())