n, k = map(int, input().split())

dp = [False] * (n+1)

cnt = 0

for i in range(2,n+1):
    if not dp[i]:
        for j in range(i, n+1, i):
            if not dp[j]:
                dp[j] = True
                cnt += 1
                if cnt == k:
                    print(j)
                    exit()