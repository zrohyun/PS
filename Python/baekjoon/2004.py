def solution():
    N, M = map(int, input().split())

    ans5 = 0
    ans2 = 0
    cnt = 1
    while True:
        t5 = [i // (5**cnt) for i in [N, M, N - M]]
        ans5 = ans5 + (t5[0] - t5[1] - t5[2])
        t2 = [i // (2**cnt) for i in [N, M, N - M]]
        if sum(t5) + sum(t2) == 0:
            break
        ans2 = ans2 + (t2[0] - t2[1] - t2[2])

        cnt += 1
    # print(ans, N // 2 - M // 2 - (N - M) // 2)
    return min(ans2, ans5)


ans = solution()
print(ans)
