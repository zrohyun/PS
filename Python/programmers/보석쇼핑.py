import collections


def solution(gems):
    num = len(set(gems))
    min_range = int(1e10)
    ans = [int(1e10), int(1e10)]

    left = 0
    counter = collections.Counter()

    for right in range(len(gems)):
        counter[gems[right]] += 1
        right += 1
        while len(counter) == num:
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]

            left += 1

            if right - left < min_range:
                min_range = right - left
                ans = [left, right]
            elif right - left < min_range and ans[0] > left:
                ans = [left, right]

    return ans
