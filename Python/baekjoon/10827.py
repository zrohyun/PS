def solution():
    a,b = tuple(map(str, input().split()))
    
    point = len(a.replace(".",""))- a.find(".")

    ans = int(a.replace('.','')) ** int(b)
    ans = str(ans)
    splt = -int(point)*int(b)

    if len(ans) - abs(splt)+1 >= 0:
        print(ans[:splt] + '.'+ans[splt:])
    else:
        print('0.' + '0'*abs(splt) + ans)

solution()
