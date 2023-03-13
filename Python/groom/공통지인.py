N, M = map(int, input().split())

a = set([str(input()) for _ in range(N)])
b = set([str(input()) for _ in range(M)])


intersect = a.intersection(b)

if not intersect:
    print(-1)
else:
    for i in sorted(intersect):
        print(i)
