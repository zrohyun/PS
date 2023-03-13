from collections import defaultdict, deque


def solution(cacheSize, cities):
    """
    cacheSize [0,30]
    cities [0,1e5]
    """
    cache_set = set()
    cache_q = deque()
    ans = 0
    for city in map(str.lower, cities):
        if city in cache_set:
            ans += 1
            cache_q.remove(city)
            cache_q.append(city)
        else:
            cache_q.append(city)
            cache_set.add(city)
            ans += 5

            if len(cache_q) > cacheSize:
                old = cache_q.popleft()
                cache_set.remove(old)

    return ans


# def solution(cacheSize, cities):
#     import collections
#     cache = collections.deque(maxlen=cacheSize)
#     cache_set = set()
#     time = 0
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             time += 1
#         else:
#             cache.append(s)
#             time += 5

#     return time
