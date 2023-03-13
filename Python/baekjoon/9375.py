from collections import defaultdict
from itertools import combinations as comb


def solution():
    """
    패션왕 신해빈
    """
    T_case = int(input())
    for _ in range(T_case):
        clothes = defaultdict(list)
        N = int(input())
        for _ in range(N):
            cloth, cloth_type = map(str, input().split())
            clothes[cloth_type].append(cloth)

        ans = 1
        for i in clothes.values():
            ans *= len(i) + 1

        print(ans - 1)


solution()

# def solution():
#     """
#     패션왕 신해빈
#     """
#     T_case = int(input())
#     for _ in range(T_case):
#         clothes = defaultdict(list)
#         N = int(input())
#         for _ in range(N):
#             cloth, cloth_type = map(str, input().split())
#             clothes[cloth_type].append(cloth)

#         ans = sum([len(i) for i in clothes.values()])
#         for i in range(2, len(clothes) + 1):
#             for j in comb(clothes.keys(), i):
#                 case = 1
#                 for c in j:
#                     case *= len(clothes[c])

#                 ans += case

#         print(ans)

#     return ans


# solution()
