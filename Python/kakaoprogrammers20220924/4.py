from math import ceil, floor, log2


def solution(numbers):
    # answer = [-1] * len(numbers)
    answer = []
    for i_n, num in enumerate(numbers):
        if num in [1, 2, 3]:
            answer.append(True)
            continue

        a = "{0:b}".format(num)
        for i in range(1, 100):
            if (2**i - 1) == len(a):
                break
            elif (2**i - 1) < len(a) < (2 ** (i + 1) - 1):
                a = "0" * (2 ** (i + 1) - 1 - len(a)) + a
                break
            else:
                continue
        answer.append(check_tree(a))
    answer = [a * 1 for a in answer]
    print(answer)
    return answer


def cvt_b(num):
    ret = ""
    while num > 0:
        ret = "1" + ret if num % 2 else "0" + ret
        num = int(num / 2)

    if len(ret) % 2 == 0 and ret[0] == "1":
        ret = "0" + ret

    return ret


def check_tree(b_num):

    half = int(len(b_num) / 2)
    left, right = b_num[:half], b_num[half + 1 :]

    queue = [[b_num[half], right], [b_num[half], left]]
    while queue:
        root, v = queue.pop()
        # print(root, v)
        if len(v) == 1:
            if root == "0" and root != v:
                return False
            else:
                continue

        half = int(len(v) / 2)
        left, right = v[:half], v[half + 1 :]
        if root == "0" and root != v[half]:
            return False
        queue.append([v[half], right])
        queue.append([v[half], left])
        print(queue)

    return True


solution([63, 111, 95, 1])
