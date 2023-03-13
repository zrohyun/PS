def solution():
    n = int(input())
    for i in range(n-1):
        print(" "*(n-1-i) + "*"*(i*2+1))
    stars = "*"*(n*2 -1)
    print(stars)
    for i in range(1,n):
        print(" "*i + stars[i:-i])

solution()

