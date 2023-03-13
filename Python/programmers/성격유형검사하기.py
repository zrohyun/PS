from collections import defaultdict


def solution(survey, choices):
    answer = ""
    score_dict = defaultdict(lambda: 0)
    for s, c in zip(survey, choices):
        c1, c2 = list(s)
        c = c - 4
        if c < 0:
            score_dict[c1] += -c
        else:
            score_dict[c2] += c

    print(score_dict)

    print(sorted(score_dict.items(), key=lambda x: (x[1], x[0]), reverse=True))

    return answer


solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
