def solution(n, build_frame):

    build = set()
    for x, y, a, b in build_frame:
        if b == 1:
            build.add((x, y, a))
            if not is_valid(build):
                build.remove((x, y, a))
        else:
            build.remove((x, y, a))
            if not is_valid(build):
                build.add((x, y, a))

    answer = [list(i) for i in build]
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    # print(answer)
    return answer
    # answer = [[]]
    # return answer


def is_valid(build):

    for (x, y, a) in build:
        if a == 1:  # 보
            gidoong_any_side = ((x, y - 1, 0) in build) or ((x + 1, y - 1, 0) in build)
            bo_both_side = ((x - 1, y, 1) in build) and ((x + 1, y, 1) in build)
            if not (gidoong_any_side or bo_both_side):
                return False

        else:  # 기둥

            from_bottom = y == 0
            build_on_bo = ((x - 1, y, 1) in build) or ((x, y, 1) in build)
            build_on_gidoong = (x, y - 1, 0) in build
            if not (from_bottom or build_on_bo or build_on_gidoong):
                return False

    return True


solution(
    5,
    [
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [2, 1, 0, 1],
        [2, 2, 1, 1],
        [5, 0, 0, 1],
        [5, 1, 0, 1],
        [4, 2, 1, 1],
        [3, 2, 1, 1],
    ],
)

# set 접근은 좋았지만 너무 빡빡한 예외처리를 하려고 한듯..
# def build_gidoong(x,y,build):
#     from_bottom = (y == 0)
#     build_on_bo = ((x-1,y,x,y) in build) or ((x,y,x+1,y) in build)
#     build_on_gidoong = ((x,y-1,x,y) in build)
#     if from_bottom or build_on_bo or build_on_gidoong:
#         build.add((x,y,x,y+1))

# def check_bo(x,y, build):
#     gidoong_any_side = ((x+1,y,x+1,y+1) in build) or ((x,y-1,x,y) in build)
#     bo_both_side = ((x-1,y,x,y) in build) and ((x+1,y,x+2,y) in build)

#     return gidoong_any_side or bo_both_side

# def check_gidoong(x,y,build):
#     pass

# def remove_gidoong(x,y, build):
#     build.remove((x,y,x,y+1))
#     if check_bo((x-1,))

# def build_bo(x,y,build):
#     gidoong_any_side = ((x+1,y,x+1,y+1) in build) or ((x,y-1,x,y) in build)
#     bo_both_side = ((x-1,y,x,y) in build) and ((x+1,y,x+2,y) in build)

#     if gidoong_any_side or bo_both_side:
#         build.add((x,y,x+1,y))
