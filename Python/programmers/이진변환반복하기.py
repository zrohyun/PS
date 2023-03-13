from collections import Counter


def solution(s):
    answer_cnt = 0
    answer_0 = 0
    while s != "1":
        cs = Counter(s)

        answer_0 += cs["0"]
        answer_cnt += 1

        s = bin(cs["1"])[2:]

    return answer_cnt, answer_0
