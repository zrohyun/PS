def solution():
    _, k = map(int, input().split())

    return sorted(list(map(int, input().split())))[-k]


ans = solution()
print(ans)