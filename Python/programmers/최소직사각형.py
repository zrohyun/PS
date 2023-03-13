def solution(sizes):
    hmax, wmax = 0, 0
    answer = hmax * wmax
    for height, width in sizes:

        hw = max(hmax, height) * max(wmax, width)
        wh = max(hmax, width) * max(wmax, height)
        if hw < wh:
            hmax = max(hmax, height)
            wmax = max(wmax, width)
            answer = hw
        else:
            hmax = max(hmax, width)
            wmax = max(wmax, height)
            answer = wh

    return answer

"""
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
    
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
##sum(size,[]) 문법 설명
##https://stackoverflow.com/questions/33541947/what-does-the-built-in-function-sum-do-with-sumlist
"""