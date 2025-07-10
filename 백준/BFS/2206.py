from collections import deque

n, m = map(int, input().split())

maze = [list(input().strip()) for _ in range(n)]
visit = [[[False, False] for _ in range(m)] for _ in range(n)]
dist = [[[0,0] for _ in range(m)] for _ in range(n)]
dist[0][0][0] = 1


dx = [1,0,-1,0]
dy = [0,1,0,-1]

queue = deque()
queue.append((0,0,0))
visit[0][0][0] = True

while queue:
    x,y,check = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > n-1 or nx < 0 or ny > m-1 or ny < 0: continue
        if visit[nx][ny][check]: continue
        if maze[nx][ny] == '0':
            visit[nx][ny][check] = True
            dist[nx][ny][check] = dist[x][y][check] + 1
            queue.append((nx, ny, check))
        else:
            if check:
                continue
            else:
                visit[nx][ny][1] = True
                dist[nx][ny][1] = dist[x][y][check] + 1
                queue.append((nx,ny,1))

answer = min(dist[n-1][m-1][0], dist[n-1][m-1][1]) if min(dist[n-1][m-1][1], dist[n-1][m-1][0]) != 0 else (dist[n-1][m-1][0] if dist[n-1][m-1][1] == 0 else dist[n-1][m-1][1])
if answer == 0:
    print(-1)
else:
    print(answer)
