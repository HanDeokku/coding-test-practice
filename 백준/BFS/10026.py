from collections import deque

n = int(input())

picture1 = [list(input()) for _ in range(n)]
picture2 = []
for i in range(n):
    add = []
    for j in range(n):
        if picture1[i][j] == 'R':
            add.append('G')
        else:
            add.append(picture1[i][j])
    picture2.append(add)

visit1 = [[False] * n for _ in range(n)]
visit2 = [[False] * n for _ in range(n)]

cnt1 = 0
cnt2 = 0

for a in range(n):
    for b in range(n):
        if not visit1[a][b]:
            cnt1 += 1
            queue = deque()
            queue.append((a,b))

            dx = [1,0,-1,0]
            dy = [0,1,0,-1]

            while(queue):
                x, y = queue.popleft()
        
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx > n-1 or ny > n-1: continue
                    if picture1[x][y] != picture1[nx][ny] or visit1[nx][ny]: continue
                    queue.append((nx, ny))
                    visit1[nx][ny] = True

for a in range(n):
    for b in range(n):
        if not visit2[a][b]:
            cnt2 += 1
            queue = deque()
            queue.append((a,b))

            dx = [1,0,-1,0]
            dy = [0,1,0,-1]

            while(queue):
                x, y = queue.popleft()
        
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx > n-1 or ny > n-1: continue
                    if picture2[x][y] != picture2[nx][ny] or visit2[nx][ny]: continue
                    queue.append((nx, ny))
                    visit2[nx][ny] = True

print(cnt1, cnt2)