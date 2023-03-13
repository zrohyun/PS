# def solution(people, limit):
#     """
#     condition
#     len(people) [1 , 50000]
#     weight, limit [40,240]
#     """
#
#     # sorting ascending
#     people.sort(reverse=True)  # people = sorted(people, reserse=True)
#
#     # method1 - Time Limit Exceeded[O(n^2)]
#     answer = 0
#     while len(people) > 1:
#         a = people[0]
#         b = 0
#         for i in people[1:]:
#             if a + i <= limit:
#                 b = i
#                 break
#
#         # can take two people
#         people = people[1:]
#         if b != 0: people.remove(b)
#         answer += 1
#
#     return answer + 1 if people else answer

from collections import deque
def solution(people, limit):
    """
    condition
    len(people) [1 , 50000]
    weight, limit [40,240]
    """

    # sorting ascending
    people.sort(reverse=True)  # people = sorted(people, reserse=True)
    l, r = 0, len(people)-1
    answer = 0
    while l<r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            l += 1

        answer += 1

    if l == r:
        answer += 1
    print(answer)
    return answer

assert solution([70, 50, 80, 50], 100) == 3
assert solution([70, 80, 50], 100) == 3