from collections import deque

n, m = map(int, input().split())

maze = [list(input()) for _ in range(n)]

fire = []
fire_q = deque()
fire_visit = [[False] * m for _ in range(n)]
jihoon = []
jihoon_q = deque()
jihoon_visit = [[False] * m for _ in range(n)]


for i in range(n):
    add_fire = []
    add_ji = []
    for j in range(m):
        if maze[i][j] == '#':
            add_fire.append(-1)
            add_ji.append(-1)
        elif maze[i][j] == 'J':
            add_fire.append(0)
            add_ji.append(0)
            jihoon_q.append((i,j))
            jihoon_visit[i][j] = True
        elif maze[i][j] == 'F':
            add_fire.append(0)
            add_ji.append(-1)
            fire_q.append((i,j))
            fire_visit[i][j] = True
        else:
            add_fire.append(0)
            add_ji.append(0)
    fire.append(add_fire)
    jihoon.append(add_ji)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

while fire_q:
    x, y = fire_q.popleft()

    for i in range(4):
        nx = x + dx[i]    
        ny = y + dy[i]
        if nx > n-1 or nx < 0 or ny > m-1 or ny < 0: continue
        if fire_visit[nx][ny] or fire[nx][ny] == -1: continue
        fire_visit[nx][ny] = True
        fire[nx][ny] = fire[x][y] + 1
        fire_q.append((nx, ny))

while jihoon_q:
    x, y = jihoon_q.popleft()

    for i in range(4):
        nx = x + dx[i]    
        ny = y + dy[i]
        if nx > n-1 or nx < 0 or ny > m-1 or ny < 0: continue
        if jihoon_visit[nx][ny] or jihoon[nx][ny] == -1: continue
        if fire_visit[nx][ny]:
            if jihoon[x][y] + 1 >= fire[nx][ny]: continue
        jihoon_visit[nx][ny] = True
        jihoon[nx][ny] = jihoon[x][y] + 1
        jihoon_q.append((nx, ny))

answer = 10000000

for i in range(0, m):
    if jihoon[0][i] == -1:
        continue

    if not jihoon_visit[0][i]: continue

    if answer > jihoon[0][i]:
        answer = jihoon[0][i]

for i in range(0, m):
    if jihoon[n-1][i] == -1:
        continue

    if not jihoon_visit[n-1][i]: continue

    if answer > jihoon[n-1][i]:
        answer = jihoon[n-1][i]

for i in range(1, n-1):
    if jihoon[i][0] == -1:
        continue

    if not jihoon_visit[i][0]: continue 

    if answer > jihoon[i][0]:
        answer = jihoon[i][0]

for i in range(1, n-1):
    if jihoon[i][m-1] == -1:
        continue

    if not jihoon_visit[i][m-1]: continue
    
    if answer > jihoon[i][m-1]:
        answer = jihoon[i][m-1]

if answer == 10000000:
    print("IMPOSSIBLE")
else:
    print(answer + 1)
