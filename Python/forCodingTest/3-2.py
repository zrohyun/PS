n,m,k = map(int, input().split())
#n,m,k = 5,8,3
data = list(map(int, input().split()))
#data = [2,4,5,4,6]

data.sort()

print(data[-2],data[-1])

if m >= (k+1):
    print((data[-1]*k+data[-2]) * (m//(k+1)) + data[-1] *(m%(k+1)))

else:
    print(data[-1] * m)
    
# first * (( m//(k+1) ) * k + m % (k+1)) + second * (m//(k+1))
#print(data[-1] * (( m//(k+1) ) * k + m % (k+1)) + data[-2] * (m//(k+1)))
