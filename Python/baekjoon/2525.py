m,s=list(map(int,input().split()))
C = int(input())
m = ((s+C)//60 + m)%24
s = (s+C)%60
print(m,s)