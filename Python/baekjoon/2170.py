def solution():
    n = int(input())
    table = []
    for i in range(n):
        s, e = map(int, input().split())
        if i == 0:
            table = [(s, e)]

        for j in range(len(table)):
            t1, t2 = table[j]

            if t1 <= s <= t2 or s <= t1 <= e:
                table[j] = (min(t1, s), max(t2, e))
                break

            if j == (len(table) - 1):
                table.append((s, e))

        # print(s, e, j)
    ans = sum([e - s for s, e in table])
    # print(ans)
    return ans


print(solution())
