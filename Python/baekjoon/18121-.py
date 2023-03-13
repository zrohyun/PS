
from sys import stdin
input = stdin.readline
N = int(input())
alph = [str(input().strip()) for _ in range(N)]
string = str(input().strip())
def solution():
    print()
    for n,i in enumerate(alph):
        if string.find(i) == 0: 
            # print(str(n+1)+" "+compress(string[len(i):]))
            print(compress(string[len(i):]))

def compress(string):
    stack = []
    if len(string) == 0:
        return ""
    for n,i in enumerate(alph):
        # print(string.find(i))
        if string == i:
            return str(n+1)
        elif string.find(i) == 0:
            stack.append(str(n+1)+" "+j for j in compress(string[len(i):]))

    return stack


print(solution())