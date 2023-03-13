# 모험가 길드
def tour():
    n = int(input())
    fears = list(map(int, input().split()))
    fears.sort()

    cnt = 0
    ans = 0
    for f in fears:
        cnt += 1
        if cnt >= f:
            ans += 1
            cnt = 0


def muloradd():
    s = list(map(int, input()))
    a = s[0]
    for i in s[1:]:
        if a <= 0 or i <= 0:
            a = a + i
        else:
            a = a * i
    print(a)
    return a
