from collections import deque

m, n, h = map(int, input().split())

tomato = [[list(map(int, input().split())) for i in range(n)] for j in range(h)]

queue = deque()
visit = [[[False] * m for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((i,j,k))
                visit[i][j][k] = True

dx = [1,0,-1,0]
dy = [0,1,0,-1]
dz = [1,-1]


while queue:
    z,x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > n-1 or nx < 0 or ny > m-1 or ny < 0: continue
        if visit[z][nx][ny] or tomato[z][nx][ny] == -1: continue
        tomato[z][nx][ny] = tomato[z][x][y] + 1
        queue.append((z, nx, ny))
        visit[z][nx][ny] = True

    for i in range(2):
        nz = z + dz[i]
        if nz > h-1 or nz < 0: continue
        if visit[nz][x][y] or tomato[nz][x][y] == -1: continue
        tomato[nz][x][y] = tomato[z][x][y] + 1
        queue.append((nz, x, y))
        visit[nz][x][y] = True

answer = 0
check = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                check = False
            
            if tomato[i][j][k] > answer:
                answer = tomato[i][j][k]

if check:
    if answer == 1:
        print(0)
    else:
        print(answer-1)
else:
    print(-1)