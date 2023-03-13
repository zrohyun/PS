def solution(marbles):
    from itertools import permutations as per

    max_ = [0]
    max_sub = 1e10
    visited = set()
    for i in range(1, len(marbles) + 1):
        for j in per(marbles, i):
            if j in visited:
                continue
            visited.add(j)
            mp = check_mid(j)  # mid_point
            if mp == (-1, -1):
                continue
            # print(mp, j)

            if mp[0] == mp[1]:
                left = j[: mp[0]]
                right = j[mp[0] + 1 :]
            else:
                left = j[: mp[0] + 1]
                right = j[mp[1] :]
            sub = abs(len(left) - len(right))

            cond1 = (sub < msub)
            cond2 = (sub == msub and len(max_) < len(j))
            cond3 = (sub == msub and len(max_) == len(j) and sum(max_) < sum(j))
            cond4 = (sub == msub and len(max_) == len(j) and sum(max_) == sum(j))
            
            if cond1 or cond2 or cond3:
                max_ = j
                msub = sub
            elif cond4:
                max_ = sorted([max_, j])[0]

            # print(max_, msub)
    # print(max_)
    return max_


def check_mid(marbles):
    left = 0
    right = sum(marbles)
    for i in range(len(marbles)):
        mid = marbles[i]
        if left == right:
            return i - 1, i
        if left == right - mid:
            return i, i
        left += mid
        right -= mid

    return -1, -1


a = solution([5, 5, 1, 4])
a = solution([1, 2, 3, 4, 4])
a = solution([3, 9, 7, 5])
print(a)
