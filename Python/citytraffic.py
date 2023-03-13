from collections import defaultdict


def CityTraffic(strArr):
    board = defaultdict(dict)
    for st in strArr:
        s, d = int(st[0]), int(st[3])
        board[s][d] = s
        board[d][s] = d

    ans = []

    for bk in board.keys():
        q = [(int(bk), k) for k in board[bk].keys()]
        visit = {k: False for k in board.keys()}
        for a, b in q:
            visit[a] = True
        traffic = 0

        while q:
            s, d = q.pop()
            visit[d] = True
            traffic += d
            for src, des in board[d].items():
                if not visit[src]:
                    q.append((des, src))

        ans.append((int(bk), traffic))

    ans.sort()



    print(ans,traffic)

    print(board)

    # code goes here
    return strArr


# keep this function call here
print(CityTraffic(["1:[5]", "2:[5]", "3:[5]", "4:[5]", "5:[1,2,3,4]"]))