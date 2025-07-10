t = int(input())

nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(t):
    new_nums = []
    case = input().split()
    sarr = input().split()
    for s in sarr:
        for i in range(10):
            if s == nums[i]:
                new_nums.append(i)
                break
    
    new_nums.sort()
    print(case[0])
    for num in new_nums:
        print(nums[num], end=' ')