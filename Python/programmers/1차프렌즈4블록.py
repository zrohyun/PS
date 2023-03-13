from collections import deque, defaultdict


def solution(m, n, board):
    answer = 0
    recon = [deque([board[i][j] for i in range(m)][::-1]) for j in range(n)]
    # recon.shape = (n,m)

    while True:
        if (temp := bomb_block(recon)) != 0:
            answer += temp
        else:
            break

    return answer


def bomb_block(board):
    log = defaultdict(set)
    cnt = 0
    for i in range(len(board) - 1):
        for j in range(len(board[i]) - 1):
            if j == len(board[i + 1]) - 1 or len(board[i + 1]) == 0:
                break
            f4b = set(
                [board[i][j], board[i][j + 1], board[i + 1][j], board[i + 1][j + 1]]
            )
            if len(f4b) == 1:
                log[i].update([j, j + 1])
                log[i + 1].update([j, j + 1])

    for i, js in log.items():
        for j in sorted(js, reverse=True):
            cnt += 1
            del board[i][j]

    return cnt


# solution(4, 5, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
a = solution(6, 6, ["IIIIOO", "IIIOOO", "IIIOOI", "IOOIII", "OOOIII", "OOIIII"])
a = solution(5, 6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"])
a = solution(
    8, 5, ["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"]
)
a = solution(2, 4, ["baab", "baab"])
print(a)
