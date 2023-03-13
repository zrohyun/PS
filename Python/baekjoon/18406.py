def solution():
    score = str(input())
    left = sum([int(i) for i in score[: len(score) // 2]])
    right = sum([int(i) for i in score[len(score) // 2 :]])
    return "LUCKY" if left == right else "READY"


solution()
