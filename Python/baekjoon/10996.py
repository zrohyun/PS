def solution():
    n = int(input())
    
    # print(stars)
    for _ in range(n):
        print("* "*(n-n//2))
        print(" *"*(n//2))

solution()

# 1
# 2 - 1
# 3 - 3
# 4 - (4//2 + 1)*2-1
# 5 - (5//2 + 1)*2-1