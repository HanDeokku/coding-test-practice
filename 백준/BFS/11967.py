from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

light = [[[] for _ in range(n)] for _ in range(n)]
arr = [[False] * n for _ in range(n)]
visit = [[False] * n for _ in range(n)]

for _ in range(m):
    x, y, a, b = map(int, input().split())
    light[x-1][y-1].append((a-1,b-1))

q = deque()
q.append((0,0))
arr[0][0] = True
visit[0][0] = True

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for a, b in light[0][0]:
    arr[a][b] = True

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if nx > n-1 or nx < 0 or ny > n-1 or ny < 0: continue
        if not visit[nx][ny] and arr[nx][ny]:
            visit[nx][ny] = True
            q.append((nx,ny))

            for a,b in light[nx][ny]:
                arr[a][b] = True

                for j in range(4):
                    ax = dx[j] + a
                    by = dy[j] + b
                
                    if not ((0 <= ax <= n-1) and (0 <= by <= n-1)): continue
                    if visit[ax][by] and arr[ax][by]:
                        q.append((ax,by))

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            cnt += 1

print(cnt)