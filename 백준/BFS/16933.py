from collections import deque
import sys

n, m, k = map(int, sys.stdin.readline().split())

maze = [list(sys.stdin.readline()) for _ in range(n)]
visit = [[[False] * (k+1) for _ in range(m)] for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

q = deque()
q.append((0,0,0,1)) # 시작위치, 벽 부순 수, 거리
visit[0][0][0] = True


while q:
    x,y,cnt,dist = q.popleft()
    
    if x==n-1 and y==m-1:
        print(dist)
        break

    day = dist % 2
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if nx > n-1 or nx < 0 or ny > m-1 or ny < 0: continue
        
        if maze[nx][ny] == '0' and not visit[nx][ny][cnt]:
            q.append((nx,ny,cnt,dist+1))
            visit[nx][ny][cnt] = True
        
        elif maze[nx][ny] == '1' and cnt < k and not visit[nx][ny][cnt+1]:
            if day:
                q.append((nx,ny,cnt+1,dist+1))
                visit[nx][ny][cnt+1] = True
            else:
                q.append((x,y,cnt,dist+1))
else:
    print(-1)