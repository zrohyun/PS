def solution():
    s = input()
    arr = str_parse(s)[::-1]

    ans = arr.pop()
    minus_sum = 0
    flag_minus = False
    while len(arr) >= 1:
        a = arr.pop()

        # -  appear
        if a=='-' and flag_minus:
            ans -= minus_sum
            minus_sum = 0
        elif a == '-' or flag_minus :
            minus_sum += a if type(a) is int else 0
            flag_minus = True
        elif a == "+":
            ans += arr.pop()
        

    return ans - minus_sum
            
def str_parse(s):
    
    arr = []

    tmp = ''
    for i in s:
        if not i.isnumeric():
            arr.append(int(tmp))
            arr.append(i)
            tmp = ''
        else:
            tmp += i

    arr.append(int(tmp))

    return arr

print(solution())

# other solution
def solution2():
    x = str(input()).split('-')
    nums = [add_splt_nums(i) for i in x]

    if len(nums) == 1: return nums[0]
    else:
        return nums[0] - sum(nums[1:])
    
    
def add_splt_nums(arr):
    ans = 0
    for i in arr.split("+"):
        ans += int(i)
    return ans

print(solution2())
