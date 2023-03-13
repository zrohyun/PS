def solution(samDaily, kellyDaily, difference):
    # Write your code here
    # sam = samDaily * x + difference
    # kelly = kellyDail * x

    init = difference + samDaily - kellyDaily
    diff = samDaily - kellyDaily
    print(init, diff)
    if diff >= 0:
        return -1

    if init < 0:
        return 1
    ans = 1
    while True:
        ans += 1
        init += diff
        if init < 0:
            return ans


print(solution(1, 2, 3))
