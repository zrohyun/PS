from collections import defaultdict


def solution(record):
    answer = []
    leave = lambda x: f"{x}님이 나갔습니다."
    enter = lambda x: f"{x}님이 들어왔습니다."
    nick_dict = defaultdict(str)
    ans = []
    for i in record:
        op, *id_nick = i.split()

        if len(id_nick) == 1:
            id_ = id_nick[0]
        else:
            id_, nick = id_nick
            nick_dict[id_] = nick
        if op == "Enter":
            ans.append((enter, id_))
        elif op == "Leave":
            ans.append((leave, id_))
        elif op == "Change":
            pass
        else:
            raise ValueError()

    return [a(nick_dict[b]) for a, b in ans]
