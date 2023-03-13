directions = {
    "r": (0, 1),
    'ld': (1, -1),
    'd': (1, 0),
    'rd': (-1, 1)
}

def is_out_of_bound(r, c, nr, nc):
    if 0 <= nr < r and 0 <= nc < c:
        return False
    return True

def BE2ndDiagonal(strArr):
    d = 'r'
    r, c = len(strArr), len(strArr[0])
    nr, nc = 0, 0
    ans = [strArr[nr][nc]]

    while True:
        if (nr == 0 and nc != (c - 1)) or nr == (r - 1):
            if (nr == 0 and nc != (c - 1)):
                d = 'ld'
            else:
                d = "rd"
            nr += directions['r'][0]
            nc += directions['r'][1]
            ans.append(strArr[nr][nc])

        elif nc == (c - 1) or (nc == 0 and nr != (r - 1)):
            if (nc == 0 and nr != (r - 1)):
                d = 'rd'
            else:
                d = "ld"
            nr += directions['d'][0]
            nc += directions['d'][1]
            ans.append(strArr[nr][nc])

        if ((nr == (r - 1)) and (nc == (c - 1))):
            break

        nr += directions[d][0]
        nc += directions[d][1]
        ans.append(strArr[nr][nc])

    return ans

# keep this function call here
print(BE2ndDiagonal([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]))