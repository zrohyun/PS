N = int(input())
X = list(map(int,input().split()))

li = []
for i in range(len(X)):
      li.append([X[i],i])
li.sort()
sort_index = []
  
for x in li:
    sort_index.append(x[1])
  
val = 0
before = X[sort_index[0]]
X[sort_index[0]] = val

for i in sort_index[1:]:
    if before == X[i]: 
        X[i] = val
        continue
    before = X[i]
    val += 1
    X[i] = val


X = list(map(str,X))
print(" ".join(X))

## other solution
# #n = int(input())
# nums = list(map(int, input().split()))
# numsS = sorted(list(set(nums)))
# indexes = dict()
# count = 0

# for i in numsS:
#     indexes[i] = count
#     count += 1

# print(' '.join(map(lambda x : str(indexes[x]), nums)))