def solution():
    N,K = map(int,input().split())
    nums = list(map(int,input().split()))

    rng_sum = sum(nums[:K])
    max_ = rng_sum
    

    for i in range(K,N):
        rng_sum = rng_sum + nums[i] - nums[i-K]
        if max_ < rng_sum:
            max_ = rng_sum
    
    print(max_)

solution()
