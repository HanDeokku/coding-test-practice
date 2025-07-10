from collections import deque

n, k = map(int, input().split())

dp = [None] * 100001

dp[n] = 0

queue = deque()
queue.append(n)

while queue:
    if dp[k] != None:
        break
    
    x = queue.popleft()

    if x+1 < 100001 and dp[x+1] == None:
        queue.append(x+1)
        dp[x+1] = dp[x] + 1

    if x-1 >= 0 and dp[x-1] == None:
        queue.append(x-1)
        dp[x-1] = dp[x] + 1
    
    if x*2 < 100001 and dp[x*2] == None:
        queue.append(2*x)
        dp[x*2] = dp[x] + 1

print(dp[k])