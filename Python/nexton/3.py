# Compiled successfully.11/15 test cases passed
def solution(initial_players, new_players, rank):
    # Write your code here
    initial_players.sort()
    print(initial_players, new_players, rank)

    ans = 0
    ap = []
    for i in range(-1, len(new_players)):
        print(ans)
        l = len(initial_players) - 1
        r = rank
        if i >= 0:
            ap.append(new_players[i])
            ap.sort()

        while r > 0:
            if i >= 0 and ap[i] > initial_players[l]:
                r -= 1
                if r == 0:
                    ans += ap[i]
                    break
                i -= 1
            else:
                r -= 1
                if r == 0:
                    ans += initial_players[l]
                    break
                l -= 1

    return ans


print(solution([1, 2, 3], [6, 5, 4], 1))
