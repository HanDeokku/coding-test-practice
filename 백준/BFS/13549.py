from collections import deque

n, k = map(int, input().split())

visited = [False] * 100001
time = [0] * 100001

queue = deque()
queue.append(n)
visited[n] = True

while queue:
    x = queue.pop()

    if x == k:
        print(time[x])
        break

    for nx in [2*x, x-1, x+1]:
        if 0 <= nx < 100001 and not visited[nx]:
            visited[nx] = True
            if nx == x*2:
                time[nx] = time[x]
                queue.append(nx)
            else:
                time[nx] = time[x] + 1
                queue.appendleft(nx)