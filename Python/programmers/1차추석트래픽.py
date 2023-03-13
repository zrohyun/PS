# from collections import defaultdict
from heapq import heappush, heappop
import heapq
from decimal import Decimal


def solution(lines):
    sorted_list = []
    for i in map(stlog2int, lines):
        sorted_list.append((i[0] + 1 - i[1], i[0]))
        sorted_list.append((i[0], i[0] + 1 - i[1]))
    answer = 0
    sorted_list.sort()
    # print(sorted_list)
    for i in range(len(sorted_list)):
        st_time = sorted_list[i][0]
        inner_set = set()
        for j in range(i, len(sorted_list)):

            if st_time + 999 < sorted_list[j][0]:
                break

            inner_set.add((min(sorted_list[j]), max(sorted_list[j])))
        # print(inner_set)
        # print(len(inner_set))
        answer = max(answer, len(inner_set))
    return answer


def stlog2int(stlog):
    st_time, run_time = stlog.split()[1:]
    h, m, s = map(Decimal, st_time.split(":"))
    st_time = h * 3600000 + m * 60000 + s * 1000
    return int(st_time), int(Decimal(run_time[:-1]) * 1000)


assert solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]) == 2
assert solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]) == 1
assert (
    solution(
        [
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s",
        ]
    )
    == 7
)
