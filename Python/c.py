import re
def solution(registered_list, new_id):
    answer = ''
    idx = find_digit_idx(new_id)
    if idx == -1:
        S,N = new_id,0

    else:
        S,N = new_id[:idx],int(new_id[idx:])

    # filter only nums
    nums = set()
    depart_nums(nums,S,registered_list)
    
            
    if N not in nums:
        return new_id
    
    while N in nums:
        N +=1
    
    return S+str(N)

def depart_nums(nums, S,registered_list):
    for i in registered_list:
        if S in i:
            idx_ = find_digit_idx(i)

            # 숫자가 없을 때
            if idx_ == -1:
                if S == i:
                    nums.add(0)
            
            # 숫자가 있으면 string 부분은 같아야함.
            elif S == i[:idx_]:
                nums.add(int(i[idx_:]))



def find_digit_idx(s):
    m = re.search(r"\d", s)

    idx = -1
    if m:
        return m.start()

    return idx


