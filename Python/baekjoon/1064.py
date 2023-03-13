from math import sqrt
def solution():
    xa,ya,xb,yb,xc,yc = list(map(int,input().split()))

    if (len(set([xa,xb,xc])) ==1 ) or (len(set([ya,yb,yc])) == 1):
        return -1.0 

    if len(set([xa,xb,xc])) != 2:
        if  ((ya-yb)/(xa - xb)) == ((yb-yc)/(xb-xc)):
            return -1.0


    com1 = sqrt((xa-xb)**2 + (ya-yb)**2) * 2 + sqrt((xa-xc)**2 + (ya-yc)**2) *2
    com2 = sqrt((xc-xb)**2 + (yc-yb)**2) * 2 + sqrt((xa-xc)**2 + (ya-yc)**2) *2
    com3 = sqrt((xb-xa)**2 + (yb-ya)**2) * 2 + sqrt((xb-xc)**2 + (yb-yc)**2) *2
    
    return max(com1,com2,com3) - min(com1,com2,com3)


print(solution())
