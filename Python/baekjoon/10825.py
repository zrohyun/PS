def solution():
    import sys

    input = sys.stdin.readline
    student = []
    for _ in range(int(input())):
        name, guk, en, math = list(map(str, input().split()))
        student.append((-int(guk), int(en), -int(math), name))

    print("\n".join([s[3] for s in sorted(student)]))


solution()
