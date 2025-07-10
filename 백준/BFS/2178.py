from collections import deque

n, m = map(int, input().split())

maze = [list(input()) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

queue = deque([(0,0)])
visit[0][0] = 1

while queue:
    x, y = queue.popleft()
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
        if maze[nx][ny] == '0' or visit[nx][ny] != 0: continue
        visit[nx][ny] = visit[x][y] + 1
        queue.append((nx, ny))
    
print(visit[n-1][m-1])