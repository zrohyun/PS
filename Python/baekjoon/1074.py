def solution():
    n,r,c = list(map(int,input().split()))
    # n=4,16*16 -> 4분할 64개
    # n=3,8*8 -> 4분할 16개
    # n=2,4*4 -> 4분할 4

    # n,r,c
    # 2,3,1 == 11
    # 원래 좌표가 있던 위치에서 보존되는 크기(2사분면은 4, 
    # 3사분면은 8 같은 크기를 보존하고 점점 좌표를 줄여가면 될듯

    print(z(2**n,r,c))

def z(n,r,c):
    ans = 0    
    while True:
        if r == 0 and c == 0: break
        quarter_len =  n // 2

        # if c//quarter_len and r//quarter_len:
        #      ans += (quarter_len**2)*3
        if c // quarter_len:
            ans += quarter_len**2
        if r // quarter_len:
            ans += (quarter_len**2)*2

        r,c = r%(n//2),c%(n//2)
        n = quarter_len
    return ans


solution()