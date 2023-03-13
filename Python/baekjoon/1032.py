def solution():
    files = []
    for _ in range(int(input())):
        files.append(str(input()))
    # print(files)
    comp = list(files[0])

    for i in files[1:]:
        for idx in range(len(comp)):
            if comp[idx] != i[idx]:
                comp[idx] = '?'

    return "".join(comp)

print(solution())