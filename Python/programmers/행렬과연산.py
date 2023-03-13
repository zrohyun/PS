def solution2(rc, operations):
    def solution(rc, operations):
        row, col = len(rc), len(rc[0])
        coord = [[[i, j] for j in range(col)] for i in range(row)]

        for o in operations:
            if o == "Rotate":
                rotate(coord, row, col)
            else:
                shiftrow(coord, row, col)

            print(coord)

        answer = [[0] * col for i in range(row)]

        for r, c in zip(rc, coord):
            for v, (y, x) in zip(r, c):
                answer[y][x] = v
        print(answer)
        return answer

    def shiftrow(coord, row, col):
        for r in range(row):
            for c in range(col):
                y, x = coord[r][c]
                if y == (row - 1):
                    coord[r][c] = [0, x]
                else:
                    coord[r][c] = [y + 1, x]

    def rotate(coord, row, col):
        for r in range(row):
            for c in range(col):
                y, x = coord[r][c]
                if y == 0:  # 맨 윗줄
                    if x == (col - 1):
                        y = y + 1
                    else:
                        x = x + 1
                elif y == (row - 1):

                    if x == 0:
                        y = y - 1
                    else:
                        x = x - 1

                elif x == (col - 1):
                    y = y + 1

                elif x == 0:
                    y = y - 1
                coord[r][c] = [y, x]

    return solution(rc, operations)


# solution(
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
# ["ShiftRow", "Rotate", "ShiftRow", "Rotate"],
# )


def soltuion1(rc, operations):
    def solution(rc, operations):
        row, col = len(rc), len(rc[0])
        answer = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                y, x = i, j
                for o in operations:
                    if o == "Rotate":
                        y, x = rotateXY(y, x, row, col)
                    else:
                        y, x = shiftrowYX(y, x, row, col)

                answer[y][x] = rc[i][j]

        return answer

    def shiftrowYX(y, x, row, col):
        if y == (row - 1):
            return 0, x
        else:
            return y + 1, x

    def rotateXY(y, x, row, col):

        if y == 0:  # 맨 윗줄
            if x == (col - 1):
                y = y + 1
            else:
                x = x + 1
        elif y == (row - 1):

            if x == 0:
                y = y - 1
            else:
                x = x - 1

        elif x == (col - 1):
            y = y + 1

        elif x == 0:
            y = y - 1
        return y, x

    return solution(rc, operations)


solution2(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    ["ShiftRow", "Rotate", "ShiftRow", "Rotate"],
)

def solution3(rc,operations):
    from collections import deque
    def solution(rc, operations):
        middle = deque()
        left,right = deque(),deque()
        for i in rc:
            l,*m,r = i
            left.append(l)
            right.append(r)
            middle.append(deque(m))
       
        def rotate():
            middle[0].appendleft(left.popleft())
            right.appendleft(middle[0].pop())
            middle[-1].append(right.pop())
            left.append(middle[-1].popleft())

        def shiftrow():
            left.appendleft(left.pop())
            right.appendleft(right.pop())
            middle.appendleft(middle.pop())
        
    
        for o in operations:
    
            if o == 'Rotate':
                rotate()
            else:
                shiftrow()
    