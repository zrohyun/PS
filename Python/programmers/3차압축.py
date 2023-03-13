def solution(msg):
    answer = []
    word_map = {chr(i): i - 64 for i in range(65, 91)}
    cnt = 26
    while msg:
        a, *msg = msg

        # 알파벳 뽑아 등록됐으면 다음 것도 뽑아
        # 등록 안됐으면 등록하고 이전에 등록됐던 알파벳 변환
        while a in word_map and len(msg) > 0:
            if a + msg[0] not in word_map:
                cnt += 1
                word_map[a + msg[0]] = cnt
                break

            a += msg[0]
            msg = msg[1:]

        answer.append(word_map[a])

    return answer


assert solution("KAKAO") == [11, 1, 27, 15]
assert solution("TOBEORNOTTOBEORTOBEORNOT") == [
    20,
    15,
    2,
    5,
    15,
    18,
    14,
    15,
    20,
    27,
    29,
    31,
    36,
    30,
    32,
    34,
]
