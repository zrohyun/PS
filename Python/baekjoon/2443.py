def solution():
    n = int(input())
    for i in range(1,n):
        print("*"*i)
    stars = "*"*(n)
    print(stars)
    for i in range(1,n):
        print(stars[i:])

solution()
