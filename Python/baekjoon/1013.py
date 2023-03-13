import re
from sys import stdin
input = stdin.readline
def solution():
    n = int(input())
    case = [str(input().strip()) for _ in range(n)]
    for i in case:
        
        p = re.compile('(100+1+|01)+')
        if p.fullmatch(i):
            print("YES")
        else:
            print("NO")

def solution1():
    n = int(input())
    case = [str(input().strip()) for _ in range(n)]
    for i in case:
        print(myre(i))

def myre(string):
    while string:
        if string.startswith("01"):
            string = string[2:]

        elif string.startswith("100"):
            string = string[3:]
            while string:
                if string[0] == '0':
                    string = string[1:]
                else: break
            if not string: return "NO"
            cnt = 0
            while string:
                if string[0] == '1': 
                    string = string[1:]
                    cnt += 1
                else: break

            if string.startswith("00") and cnt > 1:
                string = '1' + string
            elif string.startswith("01"):
                pass
            elif not string: return "YES"
            else:
                return "NO"
            
        else:
            return "NO"
    
    return "YES"
        


solution1() 

# other solution
# import re
# for s in[*open(0)][1:]:print(re.match('(100+1+|01)+$',s)and"YES"or"NO")