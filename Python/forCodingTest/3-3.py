
m,n = map(int, input().split())
res = 0

# testcase
# M,N = 3,3
# data = [[3,1,2],[4,1,4],[2,2,2]]

# for sub_list_ in data:
#     res = max(res,min(sub_list_))

for i in range(N):
    input_list_ = list(map(int, input().split()))
    res = max(res,min(input_list_))

print(res)
    
