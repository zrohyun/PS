def solution():
    dh = list(map(int, input().split()))
    right_set = [1, 1, 2, 2, 2, 8]

    return " ".join([str(a - b) for a, b in zip(right_set, dh)])


ans = solution()
print(ans)
