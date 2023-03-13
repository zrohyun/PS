def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    str1_ = [str1[i : i + 2] for i in range(len(str1) - 1) if str1[i : i + 2].isalpha()]
    str2_ = [str2[i : i + 2] for i in range(len(str2) - 1) if str2[i : i + 2].isalpha()]
    answer = J(str1_, str2_)

    return int(answer * 65536)


from collections import Counter


def J(A, B):

    if not A and not B:
        return 1

    ca = Counter(A)
    cb = Counter(B)
    inter_set = set(ca.keys()).intersection(cb.keys())
    union_set = set(ca.keys()).union(cb.keys())
    print(inter_set, union_set)
    a = sum([min(ca[i], cb[i]) for i in inter_set])
    b = (
        sum(ca[i] for i in set(set(ca.keys()) - inter_set))
        + sum(cb[i] for i in set(set(cb.keys()) - inter_set))
        + sum([max(ca[i], cb[i]) for i in inter_set])
    )
    return a / b


# def solution(str1, str2):
#     # make sets
#     s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
#     s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
#     if not s1 and not s2:
#         return 65536
#     c1 = Counter(s1)
#     c2 = Counter(s2)
#     answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
#     return answer
