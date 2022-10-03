# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6

    A = {i: 1 for i in A if i > 0}

    if len(A) == 0:
        return 1

    for i in range(1, len(A.keys()) + 1):
        if i in A:
            continue
        else:
            return i

    return i + 1


data = [[1, 3, 6, 4, 1, 2], [1, 2, 3], [-1, -3]]
print(solution(data[0]))
