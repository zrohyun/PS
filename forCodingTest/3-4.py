#m,n = map(int, input().split())
N,K = 25,3
res = 0
    
def recur(N):
    
    #base case return
    if N == 0: return 1233456789
    elif N == 1: return 0
    elif N == K: return 1
    
    a = recur(N//K) + N%K + 1
    b = recur(N-1) + 1
    
    return min(a,b)

#print(recur(N))

while True:
  target = (N//K) *K
  result += (N - target)
  
  if N < K: break

  res += 1
  N //= K

res += N

print(res)
