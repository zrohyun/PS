def solution(phone_book):
    answer = True
    pb = sorted(phone_book, key = lambda x: len(x))
    str_len = set([len(x) for x in pb])
    # 1.
    # for i in range(len(pb)):
    #     for j in range(i+1,len(pb)):
    #         if pb[j].startswith(pb[i]):
    #             return False
    
    # 3.
    # for i in range(len(pb)-1):
    #     print(pb[i], pb[i+1][:len(pb[i])])
    #     if pb[i] == pb[i+1][:len(pb[i])]:
    #         return False
    # 4.
    # phone_book.sort()
    # # print(phone_book)
    # for a, b in zip(phone_book, phone_book[1:]):
    #     if b.startswith(a):
    #         return False
    # 2.
    check = {x:1 for x in pb}
    
    for i in str_len:
        t = [s for s in pb if len(s) > i]
        for j in t:
            if j[:i] in check:
                return False
                

    return answer