def solution():
    N = int(input())
    for _ in range(N):
        pn = int(input())
        a = [0,1,1,1,2,2,3,4,5,7,9]
        if pn > 10:
            num = 11
            while num <= pn:
                a.append(a[num-1] + a[num-5])
                num+=1
        
        print(a[pn])

solution()