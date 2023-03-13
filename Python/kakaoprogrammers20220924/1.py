import math


def solution(today, terms, privacies):
    answer = []
    terms_dict = {k: int(t) for k, t in map(str.split, terms)}
    print(today, terms_dict, privacies)
    for i, p in enumerate(privacies, start=1):
        p, p_type = p.split()
        days = cal_days(today, p.split()[0])
        if terms_dict[p_type] <= math.floor(days / 28):
            answer.append(i)

    print(answer)
    return answer


def cal_days(t, p):
    yt, mt, dt = list(map(int, t.split(".")))
    yp, mp, dp = list(map(int, p.split(".")))
    y = (yt - yp) * 12 * 28
    m = (mt - mp) * 28
    d = dt - dp
    print(y, m, d, y + m + d)
    return y + m + d


solution(
    "2020.01.01",
    ["Z 3", "D 5"],
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"],
)
