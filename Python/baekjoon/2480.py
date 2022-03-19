#주사위 세개
a = list(map(int,input().split()))
if len(set(a)) == 1:
    print(10000 + set(a)[0]*1000)
elif len(set(a)) == 3:
    print(max(a)*100)
else:
    print((sum(a) - sum(set(a)))*100 + 1000)