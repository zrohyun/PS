def solution():
    R, C, K = map(int, input().split())
    loc = set()
    for r in range(R):
        temp = list(map(str, input()))
        for c, n in enumerate(temp):
            if n == "#":
                loc.add((r, c))
    # 각 점마다  퍼지는 범위가 있음.
    # 교차지점에  대한  고려가 필요할  듯


solution()
