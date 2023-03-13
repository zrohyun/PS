from itertools import combinations as comb
from collections import namedtuple
Points = namedtuple('Points', ['xs', 'ys','xys'])
def solution(line):
    
    xs = []
    ys = []
    xys = set()
    for i,j in comb(list(range(len(line))),2):
        a,b,e = line[i]
        c,d,f = line[j]
        if a*d - b*c == 0: continue
        x = (b*f - e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
        if x == int(x) and y == int(y) and (int(x),int(y)) not in xys:
            xs.append(int(x))
            ys.append(int(y))
            xys.add((int(x),int(y)))
    
    xmin = min(xs)
    ymin = min(ys)
    
    xs=[i-xmin for i in xs] 
    ys = [i-ymin for i in ys]
    xmax, ymax = max(xs), max(ys)

    points = sorted([(i,j) for i,j in zip(xs,ys)], key=lambda x: x[0])
    
    ans = [['.']*(xmax+1) for i in range(ymax+1)]
    for i,j in points:
        ans[j][i] = "*"
    
    return ["".join(i) for i in ans][::-1]