def solution():
    _ = input()
    cnt = 0
    arr =list(map(int, input().split())) 
    v = int(input())
    for i in arr:
        if v == i:
            cnt+=1
    
    print(cnt)
solution()


