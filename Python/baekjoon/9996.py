import re
def solution():
    n = int(input())
    p = str(input())
    p = re.compile(p[:p.find("*")] + "." + p[p.find("*"):])

    strings = [str(input()) for _ in range(n)]

    for i in strings:
        # print(p.match(i))
        if p.fullmatch(i):
            print("DA")
        else:
            print("NE")
def sol2():
    n = int(input())
    p = str(input())
    strings = [str(input()) for _ in range(n)]
    ppoint = p.find("*")
    for i in strings:
        if i.startswith(p[:ppoint]) and i.endswith(p[ppoint+1:]) and len(p) -1 <= len(i):
            print("DA")
        else:
            print("NE")

solution()