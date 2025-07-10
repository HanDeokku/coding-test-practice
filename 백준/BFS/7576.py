from collections import deque

m, n = map(int, input().split())

tomatos = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            queue.append((i, j))
        elif tomatos[i][j] == 0:
            visited[i][j] = -1

while queue:
    x, y = queue.popleft()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > n-1 or nx < 0 or ny > m-1 or ny < 0: continue
        if tomatos[nx][ny] != 0 or visited[nx][ny] != -1: continue
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))

check = True
answer = 0
for i in range(n):
    if not check:
        break
    for j in range(m):
        if visited[i][j] == -1:
            print(-1)
            check = False
            break
        if answer < visited[i][j]:
            answer = visited[i][j]

if check:
    print(answer)