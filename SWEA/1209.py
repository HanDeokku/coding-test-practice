for _ in range(1,2):
    case = int(input())
    nums = [list(map(int, input().split())) for i in range(100)]

    mx = 0

    for i in range(100):
        mx = max(mx, sum(nums[i]))

    for j in range(100):
        cnt1 = 0
        for i in range(100):
            cnt1 += nums[i][j]
        mx = max(mx, cnt1)
    
    cnt2 = 0
    for i in range(100):
        cnt2 += nums[i][i]
    
    mx = max(mx, cnt2)

    cnt3 = 0
    for i in range(100):
        cnt3 += nums[i][99-i]
    
    mx = max(mx, cnt3)

    print(f'#{case} {mx}')
