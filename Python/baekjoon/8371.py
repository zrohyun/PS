def solution():
    n = int(input())
    s1 = str(input())
    s2 = str(input())
    cnt = 0
    for i,j in zip(s1,s2):
        if i != j:
            cnt +=1
    return cnt
print(solution())
