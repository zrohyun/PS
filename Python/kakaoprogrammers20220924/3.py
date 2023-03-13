from itertools import combinations_with_replacement as comb

# 최적화... 존나 어렵다..
# dp로 풀어야되나?
def solution(users, emoticons):
    answer = []
    n_users = len(users)
    dc_rates = [0.9, 0.8, 0.7, 0.6]
    table = price_table(dc_rates, emoticons)

    for emo_c in comb([0, 1, 2, 3], len(emoticons)):
        bag_users = [0] * n_users
        emoji_plus = [False] * n_users
        # print(emo_c)
        for u_i, u in enumerate(users):
            # user는 본인의 기준보다 할인율이 크면은 삼.
            # 이모티콘 개수 만큼, 각각의 할인율이 있음
            for e_i, dc_i in enumerate(emo_c):
                # print(e_i, dc_i)
                if emoji_plus[u_i]:
                    break

                # user 본인의 기준보다 할인율이 크면 이모티콘 구매
                if u[0] / 100 <= (1 - dc_rates[dc_i]):
                    bag_users[u_i] += table[dc_i][e_i]

                    if bag_users[u_i] >= u[1]:
                        emoji_plus[u_i] = True
                        bag_users[u_i] = 0
                        break

        answer.append([sum(emoji_plus), sum(bag_users)])
        print(answer[-1], emo_c)
    answer = sorted(answer, key=lambda x: (x[0], x[1]), reverse=True)

    # 목적
    # sales 최대화
    # sales = 이모티콘이 할인되어 구매된 것들의 합 + 플러스를 가입한 사람들의 수
    return answer[0]


def price_table(dc, emoticons):
    table = []

    for i in dc:
        table.append([e * i for e in emoticons])
    print(table)
    return table


a = solution(
    [
        [40, 2900],
        [23, 10000],
        [11, 5200],
        [5, 5900],
        [40, 3100],
        [27, 9200],
        [32, 6900],
    ],
    [1300, 1500, 1600, 4900],
)

print(a)
