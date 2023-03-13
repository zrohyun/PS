from functools import lru_cache
@lru_cache(maxsize=None) #성공
def fibo(n):
    if n == 0 or n == 1:
        return 1
    
    return fibo(n-2) + fibo(n-1)

print(fibo(int(input()) -1))