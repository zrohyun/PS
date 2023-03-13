def solution():
    """참외밭"""
    N = int(input().rstrip())
    verti = []
    horiz = []
    directions = set([(4, 2), (2, 3), (3, 1), (1, 4)])
    direcs, lengths = [], []
    for _ in range(6):
        dirc, leng = map(int, input().split())
        if dirc in [3, 4]:
            verti.append(leng)
        else:
            horiz.append(leng)

        direcs.append(dirc)
        lengths.append(leng)
    empty = 0
    for i in range(5):
        if (direcs[i], direcs[i + 1]) not in directions:
            empty = lengths[i] * lengths[i + 1]
            break
    if empty == 0:
        empty = lengths[0] * lengths[-1]
    space = max(verti) * max(horiz) - empty
    # print(space)
    return space * N


ans = solution()
print(ans)
