def solution():
    from collections import deque
    q = deque()
    push = lambda x:q.append(x)
    pop = lambda : q.popleft() if q else -1
    front = lambda : q[0] if q else -1
    back = lambda : q[-1] if q else -1
    empty = lambda:0 if q else 1
    
    command = {
        "push": push,
        "pop":pop,
        "front": front,
        "back":back,
        "size":(lambda: len(q)),
        "empty":empty,
    }
    
    n = int(input())
    cmds = [list(map(str,input().split())) for i in range(n)]
    
    for cmd in cmds:

        if len(cmd) == 2: 
            command[cmd[0]](int(cmd[1]))
        else: 
            print(command[cmd[0]]())

solution()

"""
other solution
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

q = deque([])

for _ in range(n):
    query = input().split()
    if query[0] == 'push':
            q.append(query[1])
    elif query[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif query[0] == 'size':
        print(len(q))
    elif query[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif query[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif query[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
"""