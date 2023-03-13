from collections import defaultdict
import math


def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    ans = defaultdict(int)
    rec = defaultdict(int)
    last = 23 * 60 + 59

    for r in records:
        t, n, i = split_record(r)

        # 입차 등록
        if i == "IN":
            rec[n] = t

        # 시간 계산
        elif i == "OUT":
            time = t - rec[n]
            del rec[n]
            ans[n] += time

    for k, v in rec.items():
        ans[k] += last - v

    answer = []
    for k, v in sorted(ans.items(), key=lambda x: x[0]):
        if v <= base_time:
            answer.append(base_fee)
        else:
            fee = base_fee + math.ceil((v - base_time) / unit_time) * unit_fee
            answer.append(fee)

    print(ans)

    return answer


def split_record(record):
    time, num, inout = record.split()

    time = int(time[:2]) * 60 + int(time[3:])
    return time, num, inout
