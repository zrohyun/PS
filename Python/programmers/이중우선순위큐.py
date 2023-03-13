import collections
import heapq as hq
from collections import deque
import bisect


def solution(operations):
    answer = deque([])
    # print(type(answer))
    for operation in operations:
        op, val = operation.split()
        if op == 'I':
            bisect.insort_right(answer, int(val))
            assert isinstance(answer, collections.deque)

        elif op == 'D' and val =="1":
            if answer: answer.pop()

        elif op == "D" and val== "-1":
            if answer: answer.popleft()

        else:
            raise ValueError()

    if len(answer) == 1:
        return [answer[0], answer[0]]

    return [0, 0] if not answer else [answer[-1], answer[0]]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333","HI 1"]))