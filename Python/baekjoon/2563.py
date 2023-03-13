def solution():
    wp = [[0] * 100 for _ in range(100)]

    for _ in range(int(input())):
        X, Y = map(int, input().split())

        for y in range(Y, Y + 10):
            for x in range(X, X + 10):
                wp[y][x] = 1

    print(sum([sum(i) for i in wp]))


solution()
