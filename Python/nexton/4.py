def getMinimumHealth(initial_players, new_players, rank):
    # Write your code here
    initial_players.sort()
    print(initial_players, new_players, rank)

    ans = 0
    ap = []
    for i in range(-1, len(new_players)):
        print(ans)
        l = len(initial_players) - 1
        r = rank
        temp_ap = []
        if i >= 0:
            # ap.append(new_players[i])
            # ap.sort()
            h.heappush(ap, new_players[i])
            temp_ap = h.nlargest(r, ap)[::-1]
        j = len(temp_ap) - 1 if len(temp_ap) else -1
        while r > 0:
            if j >= 0 and temp_ap[j] > initial_players[l]:
                r -= 1
                if r == 0:
                    ans += temp_ap[j]
                    break
                j -= 1
            else:
                r -= 1
                if r == 0:
                    ans += initial_players[l]
                    break
                l -= 1

    return ans


# better
import heapq as h
import bisect


def getMinimumHealth(initial_players, new_players, rank):
    # Write your code here
    initial_players.sort()
    ans = initial_players[-rank]

    for i in new_players:
        bisect.insort(initial_players, i)
        ans += initial_players[-rank]

    return ans
