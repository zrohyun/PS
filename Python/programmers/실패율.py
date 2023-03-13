from collections import Counter


def solution(N, stages):
    cnt = Counter(stages)
    rec = [[0, 0] for _ in range(N)]
    for k, v in cnt.items():
        for i in range(N):
            if i + 1 < k:
                rec[i][0] += v
            elif i + 1 == k:
                rec[i][0] += v
                rec[i][1] += v
    rec = sorted(
        [(np / p, i + 1) if p != 0 else (0, i + 1) for i, (p, np) in enumerate(rec)],
        key=lambda x: (-x[0], x[1]),
    )
    return [i for j, i in rec]
