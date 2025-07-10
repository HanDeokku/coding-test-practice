import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]
visit = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0, 1))
visit[0][0][0] = True

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

while q:
    x, y, cnt, dist = q.popleft()

    if x == n - 1 and y == m - 1:
        print(dist) 
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < m):
            continue

        if maze[nx][ny] == '0' and not visit[nx][ny][cnt]:
            visit[nx][ny][cnt] = True
            q.append((nx, ny, cnt, dist + 1))

        elif maze[nx][ny] == '1' and cnt < k and not visit[nx][ny][cnt + 1]:
            visit[nx][ny][cnt + 1] = True
            q.append((nx, ny, cnt + 1, dist + 1))
else:
    print(-1)