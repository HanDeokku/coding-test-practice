# 직사각형을 1로 표시
# 0,0부터 0으로 표시 되어있으면 BFS 시작
# BFS 돌기 시작하면 카운트 1, 돌때마다 넓이 체크
from collections import deque

m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]
visit = [[False] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2): # (2,4)
        for j in range(x1, x2): # (0,4)
            board[i][j] = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt = 0
extents = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0 and not visit[i][j]:
            cnt += 1
            q = deque([(i,j)])
            visit[i][j] = True
            
            extent = 1

            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y

                    if nx < 0 or nx > m-1 or ny < 0 or ny > n-1: continue
                    if visit[nx][ny]: continue
                    if board[nx][ny] == 1: continue
                    
                    visit[nx][ny] = True
                    extent += 1
                    q.append((nx,ny))

            extents.append(extent)

extents.sort()
print(cnt)
for i in range(cnt):
    print(extents[i], end=" ")
